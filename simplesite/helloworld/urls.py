from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('simple', views.simple, name='simple'),
    path('', views.index, name='index'),
]