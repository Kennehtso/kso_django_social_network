from django.urls import include, path
from . import views
from . import api

urlpatterns = [
    path('', views.GeneList.as_view(), name='index'),
    path('gene/<int:pk>', views.GeneDetail.as_view(), name='gene'),
    path('list/<str:type>', views.GeneList.as_view(), name='list'),
    path('poslist/', views.GeneList.as_view(), name='poslist'),
    path('create_ec/', views.create_ec, name='create'),
    path('create_gene/', views.GeneCreate.as_view(), name='create_gene'),
    path('delete/<int:pk>', views.GeneDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.GeneUpdate.as_view(), name='update'),
    # path('api/gene/<int:pk>/update', api.gene_update),
    # path('api/gene/<int:pk>/delete', api.gene_delete),
    path('api/genes', api.GeneList.as_view(), name='genes_api'),
    path('api/gene/<int:pk>', api.GeneDetails.as_view(), name='gene_api'), # also handle GET, DELETE
    path('api/ec/<int:pk>/', api.ECDetails.as_view(), name="ec_api"),
    path('api/list/<str:type>', api.GeneList.as_view(), name='list_api'),
    path('app/', views.SPA, name="spa"),

    
]
