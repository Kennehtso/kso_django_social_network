from django.urls import include, path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'),
    path('poslist/', views.poslist, name='poslist'),
]