# Specific Validation 
1. Go to views.py
    - under a form, override the clean() function #we use cleaned_data() to access clean data
        def clean(self):
            cleaned_data = super(GeneForm, self).clean()
            entity = cleaned_data.get("entity")
            sense = cleaned_data.get("sense")

            if not entity == "Chromosome" and not entity == "Plasmid":
                raise forms.ValidationError("Entity must be 'Chromosome' or 'Plasmid'")
            if not sense == "+" and not sense == "-":
                raise forms.ValidationError("Sense must be '+' or '-'")
            return(cleaned_data)
    - then go to views.py, update the create_gene func  
        def create_gene(request):
            master_genes = Gene.objects.all()
            if request.method == 'POST':
                form = GeneForm(request.POST)
                if form.is_valid():
                    gene.save()
                    return HttpResponseRedirect('/create_gene/')
                else:
                    return render(request, 'genedata/create_gene.html', {'error': 'failed', 'master_genes': master_genes, 'form' : form} )
            else:
                form = GeneForm
            return render(request, 'genedata/create_gene.html', {'form':form, 'master_genes': master_genes})