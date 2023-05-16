from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

def index(request):
    response_string = Hello.objects.all()[0]
    return render(request, 'helloworld/index.html', {'data': response_string})

def simple(request):
    #address = Address.objects.all()
    #first_addr = address[0]
    first_addr = "first_addr TEST, not from db"
    #resident_name = str[first_addr.resident] # return the __str__
    resident_name = "first_addr.resident TEST , not from db" # return the __str__
    return render(request, "helloworld/simple.html", {"address": first_addr, "name": resident_name })
    # html = "<html><head></head><body><p>Your name is : "+ resident_name + "</br>"
    # html += "Your address is : "+ first_addr +"</p></body></html>"
    # return HttpResponse(html)
    
    # header = request.META #From django request refer to DOC.
    # ip = header["REMOTE_ADDR"]
    # html = "<html><head></head><body><p>Your ip address is : "+ ip +"</p></body></html>"
    # return HttpResponse(html, content_type="text/html", status=200) 
