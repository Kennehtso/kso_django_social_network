from django.urls import include, path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('poslist/', views.poslist, name='poslist'),
]