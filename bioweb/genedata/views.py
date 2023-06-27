from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.db import transaction

# Create Gene
class GeneCreate(CreateView):
    model = Gene
    template_name = 'genedata/create_gene.html'
    form_class = GeneForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

# Read All Gene
class GeneList(ListView):
    model = Gene
    context_object_name = 'master_genes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        if "poslist" in self.request.get_full_path():
            context['genes'] = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                context['genes'] = Gene.objects.filter(entity__exact=self.kwargs['type'])
        return context

    def get_template_names(self):
        if "poslist" in self.request.get_full_path():
             return 'genedata/list.html'
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                return 'genedata/list.html'

        return 'genedata/index.html'

# Read Detail
class GeneDetail(DetailView):
    model = Gene
    context_object_name = 'gene'
    template_name = 'genedata/gene.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

# Update Gene
class GeneUpdate(UpdateView):
    model = Gene
    fields = fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon',
              'sequencing', 'ec']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

# Delete Gene
class GeneDelete(DeleteView):
    model = Gene
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context
    
# Create ec
def create_ec(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = ECForm(request.POST)
        if form.is_valid():
            ec = EC()
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
            return HttpResponseRedirect('/create_ec/')
    else:
        ecs = EC.objects.all()
        form = ECForm()
    return render(request, 'genedata/ec.html', {'form': form, 'ecs': ecs, 'master_genes': master_genes})

def SPA(request):
    return render(request, 'genedata/spa.html')