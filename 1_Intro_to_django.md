1. TCP/IP
    - TCP: Tranmission Control Protocol
    - IP : Internet Protocol
    - 4 Layers
        1. Network Access
        2. Internet
        3. Transport
        4. Application
    - Common port
        - FTP Data :20
        - FTP contorl: 21
        - SSH: 22
        - DNS: 53
        - HTTP: 80
        - IMAP(Email): 143
        - HTTPs: 443
2. HTTP
    - Stateless request-response protocol
    - HTTP msg:
        - REQ
            1. request line
            2. req meta data
            3. blank line
            4. req body
        - RES
            1. status line
            2. res meta data
            3. blank line
            4. res body
        - http req methods
            1. GET : req resouces
            2. POST : req method
            3. PUT : send data to server
            4. DELETE : delete remote resource
        - http status code
            1xx : info
            2xx : success
            3xx : redirect
            4xx : client error
            5xx : server error

3. Component of full-stacks
   	OS	Web server	Data Store	Server-side program	Front-end framework
1	Linux	Apache	MySQL	PHP	Unspecified
2	Windows	IIS	MSQL	ASP.net	Unspecified
3	Linux	Express.js	MongoDB	js	Angular

4. Using virtual env to work with project
    1. install with:
        - pip3 install virtualenvwrapper-win (more function then venv)
    2. Create a venv:
        - mkvirtuialenv -p C:\Python310\python.exe advanced_web_dev
    3. Activate the venv
        - workon advanced_web_dev
    4. once success, you will see a bracket in front of cmd (advanced_web_dev)

5. Install django framework
    1. after workon with venv, install django
        - pip3 install django==3.0.3
    2. once installed in the venv, check pkgs
        - pip3 freeze
6. cd to target location
    1. start a django project with django-admin
        - under target location, type
            - django-admin startproject simplesite
    2. once completed, cd simplesite, should be:
        - /simplesite/simplesite/
            1. __init__.py
                - empty file that instruct python to regard this dir is a python pkg
            2. asgi file
                - contain conf require for any asgi compliant web services we might use
            3. settings.py
                -  file includes global settings for entire project
            4. urls.py
                - contain rules needed to root user requests from web server to various part of our project
            5. wsgi.py
                - contains settings to config
                interact with wsgi compliant web service
        
        - /simplesite/manage.py
            - .py copy of django admin that's pre config for our project, no django-admin need anymore,
            - we can just use manage.py for our project
7. start a new app, type
    - python manage.py startapp helloworld
    - once completed, it will created under the root of simplesite folder, along side with manage.py
    - as my observation, I think the original /simplesite/simplesite is mainly focus on api or config, setting, etc.
    - other apps like streaming, listing, detail should be create a new app along side

8. django application structure
    0. migrations folder
        - empty as initialized
        - is an model instructions for creating/modifiying 
            the database that underline our applications 
    1.  __init__.py
        - regard as a py pkgs
    2. admin.py
        -  for admin config
    3. apps.py
        - current config for app 
    4. models.py
        - write the description for our databases and our back-end
    5. tests.py
        - unit test, functional test
    6. views.py
        -   bulk of our app logic will design in the MVC pattern
        - this file will be regard as the controller
        - django is more Models views template
9. Serving the first webpage
    0. Make sure already working with virtual environment
        - to check any venv provide, run
            - workon
            # under C:\Users\{user name}\Envs\ by default
        - use the venv, run
            - workon advanced_web_dev
    *. it provide simple web server for dev purpose provided by django frameworks
    *. NEVER use dev web server for public 
        - development server is single-threaded, single-page can be handle at a time
        - if there's multiple users, they will end-up in a queue waiting for web pages
    *. Production web servers, eg: Ngix, apache are config to handle many hundreds of thousands of concurrent users
    1. goto the dir which have manage.py
    2. type python manage.py runserver 127.0.0.1:8080
    3. we should see the web server started with simple info
        - started datetime
        - ver of django & using settings (simplesite\simplesite\settings.py)
        - server url

10. Add a page to helloworld app
    1. Define DB model
        # config the db spec in model.py:
        - goto {project name}/{application name}/
        - open models.py
        # here we can create a class, and describe how a database looks like
    2. Define urls Path
        # when user make request, how to map request to code
        - use URL routing that Django provides
        - goto {project name} / {project name} 
        - open urls.py
            - import "include" functions
            - add a path, for example the root path
                - path('', include("helloworld.urls"))
        - add a new urls.py to  {project name}/{application name}/
            - import "path" functions
            - define urlpatterns for this app
                - eg: path('', views.index, name='index')
    3. Create views to actually fetch data
        - goto {project name} / {application name}
        - open views.py, here is how we get data from db
        - from .models import * # import every class 
        - define a function def index(request): to get from db and return the response
        - and return a render(request, 'helloworld/index.html', {'data': response_string}) to user

    4. Create template to display data
        - goto {project name} / {application name}
        - create folder "templates" if not existed
        - create dir, file regarding the urls in views.py
            eg: simplesite/helloworld/templates/ + /helloworld/index.html
        - add some content to index.html eg: {{ data.text}}

    5. Include application to project, 
        - goto {project name} / {project name} /
        - open settings.py
            - here are various Global config
        - look for INSTALLED_APPS variables
        -  add 'helloworld.apps.helloworldConfig' # That's define under
            - course\project\topic1\simplesite\helloworld\apps.py
    
    6. Create the table
        # we have only create the model of the table, but not the actual yet
        - go to {project name} / 
        - run command that create instruction to create table
            - python manage.py makemigrations
        - we can find migrations 0001_initial.py under  {project name} / {application name} / migrations / 
        - run command that execute the code in the migrations
            - python manage.py migrate 

    7. Populate data with json (OPTIONAL)
        # testing purpose
        - goto {project name} / {application name} /
        - create file:
            - init.json
                - there key:value
                    - "model":"helloworld.Hello",
                    - "pk":1,
                    - fields : { "text" : ... , }
        - goto {project name} / 
        - run command to load data from json
            - python .\manage.py loaddata .\helloworld\init.json
        - Now the db will init with data
        - run server and see the result
            - python manage.py runserver 127.0.0.1:8080

11. Django - Views
    - functions that recieved a web request and return web response
    - possible to move controller logic to other files,
    - use urls.py file to route web requests to any file and function of choice
    1. goto {project name} / {application name} / views.py
    2. import httpResponse
        - from django.http import HttpResponse
    3. create a new function to return a view
            def simple_view(request):
                header = request.META #From django request refer to DOC.
                ip = header["REMOTE_ADDR"]
                html = "<html><head></head><body><p>Your ip address is : "+ ip +"</p></body></html>"
                return HttpResponse(html) 
        1. this content pass to the HttpResponse is the message body
        2. HttpResponse can carry other type of data, eg: JSON, XML
        3. default return type is html data, but can be changed to mine type/media type
        4. status code by passing status=200 to HttpResponse 
        
12. Django - Model
    - python class that describe data resources, vast majority would be relational DB
    1. in dev mode: django use light-weight SQLite
        - SQLite, popular choice to store local user data in many computer games and mobile apps.
        - ease of use and setup, 
    2. Django models provide 2 interlinked pieces of functionality:
        1.  describie a DB, it's table and relationships between those tables in pure python code
            - access data access data in object-relational mapping
        2.  template of generate a database that matches description #1
        3. python manage.py makemigrations and migrate to matches the database to current models.py
    3. Some charateristics:
        - db_index optimize this table for being searched by the "name"
        - pk is added automactically in django
        - default string method def __str__(self) cast row data in string format 
        - models.ForeignKey(...) define which table is linked to the address table
            - stores a copy of a pk match Person
            - on_delete=models.SET_NULL means if delete people in the db, the address will still remain
              
13. Django - Templates
    - view of (MVC) <==> templates
    - web servers concerns to sent HTML to clients
    - data structure, content, metadata used by web browsers to define
        how to layout and display and info in user"s browser
    - goto {project name} / {application name} / views.py
    - define a function that return a render func that includes 3 parameters
        1. request: object
        2. location template to use: string
        3. content : dict
    - create a new template in {project name } / {application name} / templates /
        1. we can use {{ }} to display the data
        2. we can also use {{ name|upper }} 
    - create a base.html that for reusing in serveral html looks alike
        - create a base.html under /templates/
        - write & define the reuse part
        - for the non-reuse part use:
            1.  {% block content %}
            2.  {% endblock %}
    - go back to the specific template, REMOVE all <header>, common use tags
        1. use {% extends "helloworld/base.html"%} to tell django this page will extend base.html
            - Notice that if in {project} / {project} / settings.py
                fields'APP_DIRS' set to True,
                django will allow the templates algorithm to find specific under app.
            - so noticed that we don't need to use ./base.html or helloworld/templates/base.html when extend
        2. wrap specific content inside {% block content%} ... {% endblock %}
        
13. Django - URLS
    - when web servers recieve request, pass resources path info to the app
    - app establish, reach the main project urls.py file 
    - run the path resolution code in urls.py
    - is under {project name} / {project name} / urls.py
        - the typical use case of it is to include other urls.py file in various apps
    - project/urls.py -> helloworldApp/urls.py -> views
    -* AWARE that urls.py dispatch and pattern matchign is performed sequentially.
    - if matched before, the later pattern might not be reached
    1. add path under urlPATTERNS = [ ... ]
    2. we can include path and re_path
        - path matches simple strings
        - re_path allow to match strings with regular expression
    3. bott take 2 arguments
        1. string or pattern to match
        2. some location to dispatch
            - dispatch to function : must be package location fully specified
            - dispatch to other url file : call the include function
        3. SAMPLE:
            - path('user', helloworld.return_all)
            - path('user/int:id', helloworld.id_lookup)
            - path('user/str:name', helloworld.name_lookup)
            - re_path(r'users$', helloworld.return_all)
            - re_path(r'^user/(?P<id>\d+)$', helloworld.id_lookup)
            - re_path(r'^user/(?P<name>\w+)$', helloworld.name_lookup)
