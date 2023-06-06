1. Update urls.py
    # send various user request paths to web application
    1. go to {project name} / {project name} / urls.py
    2. import include from django.urls
    3. add path for genedata
        - path('', include('genedata.urls')), 

2. create app urls
    1. go to {project name } / {app name}
    2. create urls.py eg: /bioweb/genedata/urls.py, the add the content
        from django.urls import include, path
        from . import views

        urlpatterns= [
            path('', views.index, name='index'),
        ]
    3. update views.py
        1. go to {project name} / {app name} / views.py
            def index(request):
                response = "Hello"
                return render(request, 'genedata/index.html', {'message': response})
    4. create a html file for display
        1. go to {project name} / {app name}
        2. create new folders and subfolders 'templates/genedata/' 

    5. stop and restart server and will see 'Hello' in http://127.0.0.1:8080 
        - if it display correct which means the url mapping is correct
    
    6. Interact with database
        - go to views.py, import 
            - from .models import * 
        - update the index func
            def index(request):
                genes = Gene.objects.all() # objects.all() similar to select * from Gene
                return render(request, 'genedata/index.html', {'genes': genes})
        - Go to index.html
            - loop all items with it's gene.pk to link to another page, add this inside the html
                {% for gene in genes %}
                    <tr>
                        <td>
                        <a href="/gene/{{ gene.pk }}">{{ gene }}</a>
                        </td>
                    </tr>
                {% endfor %}

        - Since we have a new url, register url path to /genedata/urls.py
            # with this path, we will pass a expected int type call pk and runs views.gene function
            path('gene/<int:pk>', views.gene, name='gene'),
            
        - back to views.py, add
            def gene(request, pk):
                gene = Gene.objects.get(pk=pk)
                return render(request, 'genedata/gene.html', {'gene': gene})

        - and finally add a new template call gene.html

        - we can also show the ONE-TO-ONE Mapping fields such as:  ec, sequencing 
            add the following to display sequencing fields
            {% with seq=gene.sequencing %}
                <tr>
                    <td>Sequencing Factory:</td>
                    <td>{{ seq.sequencing_factory }}</td>
                </tr>
                <tr>
                    <td>Factory Location:</td>
                    <td>{{ seq.factory_location }}</td>
                </tr>
            {% endwith %}

        - for MANY-TO-MANY fields, eg: GeneAttributeLink
            add the following to display gene-attribute fields
            {% with links=gene.geneattributelink_set.all %}
                {% for link in links%}
                <tr>
                    <td>{{ link.attribute.key }}:</td>
                    <td>{{ link.attribute.value }}</td>
                </tr>
                {% endfor %}
            {% endwith %}

        - add button for filtering
            - index.html   

            - urls.py, Add path
                path('poslist/', views.poslist, name='poslist'),

            - views.py, create/update function
                def poslist(request):
                    genes =  Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
                    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList'})

            - refresh web server and checked

        