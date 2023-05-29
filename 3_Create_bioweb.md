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
    