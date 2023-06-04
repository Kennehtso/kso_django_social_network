1. Add admin user to project
    - go to {Project Name} / {Project Name app} eg: bioweb/bioweb
    # where manage.py located and ruN
    - python manage.py createsuperuser
    - name it 'admin'
    - give email, # we can use give a dummy email for dev
    - define pw: #qwer1234
2. update ALLOW_HOST in settings.py
    - add ' 127.0.0.1' or 'localhost', or other host..

3. run server # python manage.py runserver 127.0.0.1:8080
4. register our tables to admin portal for maintenence
    1. Add Gene Admin
        go to {Project Name} / {Target app name}/admin.py eg: bioweb/genedata/admin.py
        # import models
        from . models import *
        # define class for Gene admin 
        class GeneAdmin(admin.ModelAdmin):
            list_display = ('gene_id', 'entity', 'start', 'stop', 'sense')
        admin.site.register(Gene, GeneAdmin)
        # note that ForeignKey do not need to be set here
    2. once register, we can add entry to Gene tables with django admin
        - but there are some fields that are not working
            - sequencing, ec
    3. Register relevant table for Admin
        class ECAdmin(admin.ModelAdmin):
            list_display = ('ec_name', )

        class SequencingAdmin(admin.ModelAdmin):
            list_display = ('sequencing_factory', 'factory_location')
    
        admin.site.register(EC, ECAdmin)
        admin.site.register(Sequencing, SequencingAdmin)
    
    4. for MANY-TO-MANY link TABLE : GeneAttributeLink #gene, attribute
        # since this should be handle by Gene tables
        # use admin.TRabularInline
        # add a Inline Class for AttributeLink                
        class GeneAttributeLinkInline(admin.TabularInline):
            model = GeneAttributeLink
            extra = 3
        # update GeneAdmin to apply GeneAttributeLinkInline with inlines.
        class GeneAdmin(admin.ModelAdmin):
            list_display = ('gene_id', 'entity', 'start', 'stop', 'sense')
            inlines = [GeneAttributeLinkInline]

    5. DELETE content from Tables;
    # since there' refernence, need to delete table by orders
        DELETE FROM genedata_product;   
        DELETE FROM genedata_gene;
        DELETE FROM genedata_ec;
        DELETE FROM genedata_sequencing;
        DELETE FROM genedata_attribute;

    6. write a script to load data from csv
        - use the provided populate_genedata.py

