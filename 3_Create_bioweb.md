1. This readme is to demonstrate how to start a new project - bioweb
    - go to target location, run cmd:
    - django-admin startproject bioweb

2. Create a new app in bioweb project
    - go to /Project_Location/bioweb/, run cmd:
    - python manage.py startapp genedata

3. Do the typical procedure to build up components:
    1. Go to /bioweb/genedata/models.py
        - create new class based on models.Model
    2. Update models.py, add model class for further migration

4. Schema migrations
    # django default use SQLite3 as default, it can also migrate to MySQL, Postgres, etc for production
    1. go to /Project_Location/bioweb/bioweb/settings.py
    2. add pipline to INSTALLED_APPS
            ...  
        INSTALLED_APPS = [
            'genedata.apps.GeneDataConfig',
            ...
        ]
        ...
    3. Update DATABASES, using django postgressql instead of default sqlite3
        DATABASES = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bioweb_db',
            'USER': 'postgres',
            'PASSWORD': 'qwer1234',
            'HOST': 'localhost',
            'PORT': '5432', 
        }
    5. Go to command pip install psycopg2==2.8.6 (django postgres)
    5.2 update requirement.txt, run
        - pip freeze > requirements.txt
    6. Open SQL (pg-admin), and create database
        - CREATE DATABASE bioweb_db;
    7. Go to /Project_Location/bioweb/, type
        - python manage.py showmigrations
    8. if there is no error, we could see (no migrations) yet for the app
        - python manage.py makemigrations
        # this will read model's file and make code.
        # now we will find migrations for genedata app in showmigrations
    9. We can run following cmd to see what excactly the 0001_initial will do for genedata   
        model migrations
        - python manage.py sqlmigrate genedata 0001_initial
    10. Create tables with migrate cmd
        - python manage.py migrate
        # If it said UTC problem with database connection, run sql
        # SELECT * FROM pg_timezone_names;
        # ALTER DATABASE db_name SET TIMEZONE TO 'new_timezone';
        # show TIMEZONE; should be UTC
        # then restart postgressql server 10/13... service
        # try again
        # if still fail, upgrade django
        # pip install --upgrade django

    11. Update the Gene Model, add index for gene_id field, add the following attr.
        -  db_index=True

    12. New migrations after any update in the models file
        - python manage.py makemigrations
        - python manage.py showmigrations;
        - python manage.py migrate
    
    13. We can check the django migrations in db
        - select * from django_migrations where app ='genedata';
    
    14. Now the bioweb_db is build according to the django bioweb\genedata\models.py
    15. Next up we'll populate data