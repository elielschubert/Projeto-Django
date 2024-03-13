from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cliente, name='lista_cliente'),
    path('clientes/', views.lista_cliente, name='lista_cliente'),  # URL para listar clientes
    path('novo/', views.cria_cliente, name='cria_cliente'),
    path('editar/<int:pk>/', views.edita_cliente, name='edita_cliente'),
    path('deletar/<int:pk>/', views.deleta_cliente, name='deleta_cliente'),
]
