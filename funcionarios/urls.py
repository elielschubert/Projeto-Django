from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),  # URL para listar clientes
    path('novo/', views.cria_funcionario, name='cria_funcionario'),
    path('editar/<int:pk>/', views.edita_funcionario, name='edita_funcionario'),
    path('deletar/<int:pk>/', views.deleta_funcionario, name='deleta_funcionario'),
]


