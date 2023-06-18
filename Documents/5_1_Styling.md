# Styling with CSS
1.  Go to {Project } / {app}
2. create directory and files /static/css/genedata.css
3. Include css
    - Go to header.html, in <head>...</head> section, type
    <link rel="stylesheet" type="text/css" href="../static/css/genedata.css">
4. Update all main pages
    - remove repeated header, footer
    - extend {% extends "./base.html"%}
    - wrap content with {% block content %} ... {% endblock %}

5. Extract the common components from gene.html to base.html
    - wrap it with {% block geneList %} ... {% endblock % }

6. apply some css for <div id="gene_list"> ... </div> to divide the content to left and right
    - left side will be gene list appear all the time (so moved to based page, update views return objects with gene_list)
    - right side is base on the content we wanted to show

7. CSS declarication depends on Specificity, which 
    ID rules > Class Rules > Element Rules
        <main>
            <p class="classtest" > ... </p>
            <p class="classtest" id="idtest"> ... </p>
        <main>

8.1 Using Django forms object with templates
    1. go to index.html, add a button to create 'ec'
        - bioweb\genedata\templates\genedata\index.html
         <a href="/create_ec/">Add a EC Entry</a>
    
    2. go to urls.py, register a route for this action
        - path('create_ec/', views.create_ec, name='create'),
    
    3. go to views, add a fuction name def create_ec(request):
        - include all from forms.py 
    4. Create a forms.py under
        - bioweb\genedata\forms.py
        - add class to map the forms.Form
            class ECForm(forms.Form):
                ec_name = forms.CharField(label='EC Name', max_length=100)

    5. Go back to views.py, implement the logic for create_ec
        it will have 2 actions
            - POST
                - user pass 'ec_name' from forms (mapped in forms.py) TO ec.ec_name model
            - non Posst
                - user pass nth, demand a empty form
    6. Create ec.html
        - extend base.html
            {% extends "./base.html" %}
            {% load bootstrap4 %}

            {% block content %}
            <h2>Current EC Names</h2>
            <table>
            <tr><th>EC Name</th></th>
                {% for ec in ecs %}
                <tr><td>{{ ec }}</td></tr>
                {% endfor %}
            </table>
            <br />
            <h2>Add New EC Name</h2>
            <form action="/create_ec/" method="post"  class="form">
                {% csrf_token %}
                {% bootstrap_form form %}
                <input type="submit" value="Submit">
            </form>
            {% endblock%}
    
8.2 Using Django Model forms object with template
    - similar to forms but work with Django model1. 
    1. go to index.html, add a button to create 'gene'
        - bioweb\genedata\templates\genedata\index.html
         <a href="/create_gene/">Add a Gene Entry</a>
    
    2. go to urls.py, register a route for this action
        - path('create_gene/', views.create_gene, name='create'),
    
    3. go to views, add a fuction name def create_gene(request):
        - include all from forms.py 
            - so we will use 

    4. Create a forms.py under
        - bioweb\genedata\forms.py
        - add class to map the forms.Form
            class GeneForm(forms.Form):
                class Meta:
                    model =  Gene
                    # since there are fields we need to exclude, so we pick fields to return by ourselves.
                    fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'sequencing','ec']

    5. Go back to views.py, implement the logic for create_gene
        it will have 2 actions
            if request.method == 'POST':
                form = GeneForm(request.POST)
            else:
                master_genes = Gene.objects.all()
                form = GeneForm
                if form.is_valid():
                    gene = form.save()
                    return HttpReponseRedirect('/create_gene/')
            return render(request, 'genedata/create_gene.html', {'form':form, 'master_genes': master_genes})

    6. Create create_gene.html
        {% extends "./base.html" %}
        {% load bootstrap4 %}

        {% block content %}
        <h2>Add New Gene </h2>
        <form action="/create_gene/" method="post" class="form">
            {% csrf_token %}
            {% bootstrap_form form %}
            <input type="submit" value="Submit">
        </form>
        {% endblock%}

    
