1. Intro
    - when submit the mid-term
    - create a requirements.txt and list all the package inside
    - look for websinar video or install package from requirements.txt recursively
        - we can use "pip freeze > requirements.txt" to create one  

2. should be 
    zip
        - src/
        - requirements.txt

3. they will look for where the manage.py is, which should just under src/
4. they will then run "python manage.py makemigrations"
5. python manage.py migrate"
6. python manage.py runserver"
7. setup user, under where manage.py is
    - python manage.py createsuperuser
    - find more in websites.
8. Use 'django Debug Toolbar'
    - pip install django-debug-toolbar
    - then, pip freeze > requirements.txt
    1. after created app, go to setting.py
    2. installed_apps
        - leave comment to seperate custom added apps

    3. MVC 
        - once created a model,
        - go to urls.py, add an items
        - go back to settings, add middleware, put at the top
        # noted that the order is IMPORTANT, 
        - add ip address, remain to use "ALLOW_HOST" in the video?
        - 
9. mid-term, week 10