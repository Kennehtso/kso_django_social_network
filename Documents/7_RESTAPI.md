# RESTAPI
1. Representational State Transfer. 
    REST, short for Representational State Transfer, is a software and server architecture design pattern for creating web services.
    Web servers and web services adhering to this design pattern are usually called RESTful web services. 

2. Feature of REST
    1.  Client-server architecture
    2.  Statelessness
    3.  CACHEABLE
    4.  Layered System
    5.  Uniform Interface
    6.  Code-on-demand (Optional)

3. AJAX
    1. Django main server, 2 concerns
        - restAPI serves DATA
        - SPA entire web app
    2. Example:
        1. go to urls.py
            - add a path
                -    path('app/', views.SPA, name="spa"),
        2. go to views.py
            - add the SPA function   
                def SPA(request):
                    return render(request, 'genedata/spa.html')
        
        3. add a page
            - spa.html
                ** check out git **
            - refer to other pages, but remove django template rendering

        4. create spa.js
            ** check out git **

        5. back to spa.html, on the body tag, add onload="initialisePage()" 
            to tell this page to load this chunk of js when the page is finish loading

        6. Define the function first then apply the logic and actions
