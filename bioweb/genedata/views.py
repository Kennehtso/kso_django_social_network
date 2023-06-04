from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    genes = Gene.objects.all() # objects.all() similar to select * from Gene
    return render(request, 'genedata/index.html', {'genes': genes})

def gene(request, pk):
    gene = Gene.objects.get(pk=pk)
    return render(request, 'genedata/gene.html', {'gene': gene})

def poslist(request):
    genes =  Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList'})