# Templating
1. basic html intro
    - inside <head>...</head>
        1. <meta> elements
            - do not take closing tags
            - charset : define the character set interpret the page when loads the page 
            - desc for page
            - keywords for seo
            - name of author

    - inside <body>...</body>
        1. usually the main content lands here

2. Use DRY divide to reusable elements, 
    # usually divide to
    - base.html (that usually include all folloiwing components html )
        - header.html
        - title / navigator .html
        - footer.html
    
3. use {% include ".header.html "%} to include header.html in base.html
    - similar to footer.html and other components,
    - but depends on what's your strucutre, example:
        {% include './header.html' %}
        {% include './title.html' %}

        <div class="main>
            {% include './title.html' %}
            {% block content %} content will not render here {% endblock %}
            {% include './OTHER_CONTENT.html'%}
        </div>

        {% include './footer.html' %}

4. So for the real individual content pages, we can remove all duplciate components
    - There are few steps to do it:
        1. then add the following statement to extend some page for current page
            - {% extends "base.html"%}
        
        2. wrap all content with
            {% block content %} 
                ...
                all content in the current page
                ...
            {% endblock %}

    - After that, when rendering this page, it will include all components from base.html, and
        interpolate the block content from this page to base.html 

5. add template tags to reduce too much complicated logic in template html
    1. under {project} /{application}, create folder templatetags
        - create file __init__.py, mark this directory as a python package
        - create file my_tags.py
    2. case, display current date with specific format,
        1. open my_tags.py, code:
            importimport datetime
            from django import template

            register = template.Library()

            @register.simple_tag
            def todays_date():
                return datetime.datetime.now().strftime("%d %b, %Y")
        
        2. Go the the target page and import my_tags.py, eg: footer.html
            1.  open footer.html, at the top of the content, type
                {% load my_tags %}
            