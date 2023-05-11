from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    response_string = Hello.objects.all()[0]
    return render(request, 'helloworld/index.html', {'data': response_string})