# Django Generic View
1.  if using simple CRUD functions for this project / sites, we can simply apply django generic view
    - it will be logically more organized
    - easy to maintain
2. For get all fucntions
    - go to views.py and import
    - from django.views.generic import ListView
    - replace def index() ... with the following class
        class GeneList(ListView):
            model = Gene
            context_object_name = 'master_genes'
            template_name = 'genedata/index.html'

    - Go to urls.py
        - replace the 
            - path('', views.index, name='index'),
            TO
            - path('', views.GeneList.as_view(), name='index'),

3. For create one detail function (Create)
    - Go to views.py
    - from django.views.generic import CreateView
    - replace def create_gene() ... with the following class
        class GeneCreate(DetailView):
            model = Gene
            template_name = 'genedata/create_gene.html'
            # since we're using form to create
            form_class = GeneForm
            success_url = '/create_gene'

            # add the following to pass master_genes for render
            def get_context_data(self, **kwargs):
                # get the default single gene object
                context = super().get_context_data(**kwargs)
                # add a context object name master_genes
                context['master_genes'] = Gene.objects.all()
                return context
    - Go to urls.py
        - replace the 
            - path('create_gene/', views.create_gene, name='create_gene'),
            TO
            -  path('create_gene/', views.GeneCreate.as_view(), name='create_gene'),

4. For get one detail fucntion (Read)
    - Go to views.py
    - from django.views.generic import DetailView
    - replace def gene() ... with the following class
        class GeneDetail(DetailView):
            model = Gene
            context_object_name = 'gene'
            template_name = 'genedata/gene.html'
    - Go to urls.py
        - replace the 
            - path('gene/<int:pk>', views.gene, name='gene'),
            TO
            - path('gene/<int:pk>', views.GeneDetail.as_view(), name='gene'),
    - We need to override get_context_data() to pass more object for rendering
        - Back to views.py, under class GeneDetail(DetailView), add:
            def get_context_data(self, **kwargs):
                # get the default single gene object
                context = super().get_context_data(**kwargs)
                # add a context object name master_genes
                context['master_genes'] = Gene.objects.all()
                return context


6. For update one detail function (update)
    - from django.views.generic.edit import UpdateView
    - Go to gene.html, besides delete button, add 'update' button to update record correspondantly
        - <a href="/update/{{gene.pk}}">UPDATE RECORD</a>  
    - Go to urls.py
        - add path 
            -  path('update/<int:pk>', views.GeneUpdate.as_view(), name='update'),
    - Go to views.py
    - from django.views.generic import UpdateView
    - replace def gene() ... with the following class
        class GeneUpdate(UpdateView):
            model = Gene
            # specify which fields are available for update.
            fields = fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon',
                    'sequencing', 'ec']
            template_name_suffix = '_update_form'
            success_url = reverse_lazy("index")

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['master_genes'] = Gene.objects.all()
                return context
    - Create a new template file: gene_update_form.html
        {% extends "./base.html" %}
        {% block content %}
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Update">
        </form>
        {% endblock %}

    
5. For delete one detail function (Delete)
    - Go to views.py
    - from django.views.generic import DeleteView
    - replace def create_gene() ... with the following class
        class GeneDelete(DeleteView):
            model = Gene
            success_url = '/test'

            # add the following to pass master_genes for render
            def get_context_data(self, **kwargs):
                # get the default single gene object
                context = super().get_context_data(**kwargs)
                # add a context object name master_genes
                context['master_genes'] = Gene.objects.all()
                return context
    - Go to urls.py
        - replace the 
            - path('delete/<int:pk>', views.delete, name='delete'),
            TO
            -  path('delete/<int:pk>', views.GeneDelete.as_view(), name='delete'),

    - we add another templates gene_confirm_delete.html for confirming before go through the delete action successful delete
        {% extends "./base.html" %}
        {% block content %}
        <form method="post">
            {% csrf_token %}
            <p>Are you sure you want to delete "{{ object }}"?</p>
            <input type="submit" value="Confirm">
        </form>
        {% endblock %}

7. we can also refactor def list(request, type) and def poslist(request) with django generic view
    - Go to views.py, under class GeneList(ListView): we just added:
        - remove template_name since we need to determine by override fucntion get_template_names:
            template_name = 'genedata/index.html' 
            
        - override the following functions:
            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['master_genes'] = Gene.objects.all()
                if 'type' in self.kwargs:
                    if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                        context['genes'] = Gene.objects.filter(entity__exact=self.kwargs['type'])
                return context

            def get_template_names(self):
                if 'type' in self.kwargs:
                    if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                        return 'genedata/list.html'

                return 'genedata/index.html'
    - Go to urls.py
        - replace the 
            - path('list/<str: type>', views.list, name='list'),
            TO
            -  path('list/<str: type>', views.GeneList.as_view(), name='list'),
        
8. Refactoring the def poslist(request): to class GeneList(ListView)
    - add a condition inside def get_context_data(self, **kwargs):
        ...
        # if substring is include in full path
        if "poslist" in self.request.get_full_path():
            # filter genes data by field 'entity' ==  'Chromosome' and 'sense' must start with '+'
            context['genes'] = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
        ...
    - same add the return template to def get_template_names(self):
        if "poslist" in self.request.get_full_path():
            return 'genedata/list.html'

