# Update
1. Go to {Project Name} / {App Name} / models.py
    - add a new field to genes 
        ...    
        access = models.IntegerField(null=False, blank=False, default=0)
        ...

2. Go to views.py
    - under def gene plus 1 each time for gene.access for every access
        ...
        gene = Gene.objects.get(pk=pk)
        gene.access += 1
        gene.save()
        ...

3. Make migrations since new field to the models
    - python manage.py makemigrations
    - python manage.py showmigrations
    - python manage.py migrate

# Delete
4. For deleting record
    - add button in index.html
        - <a href="/delete/{{gene.pk}}">DELETE RECORD</a>
    - update urls.py
        - path('delete/<int:pk>', views.delete, name='delete'),
    - update views.py
        -  from django.http import HttpResponseRedirect
            ...
                    
        def delete(request, pk):
            # Noted that since there's MANY-TO-MANY relation between GeneAttributeLink and Gene, we need to delete relevant records from it first, then delete from Gene
            GeneAttributeLink.objects.filter(gene_id=pk).delete()
            Gene.objects.filter(pk=pk).delete()
            # redirect to index page
            return HttpResponseRedirect("/")