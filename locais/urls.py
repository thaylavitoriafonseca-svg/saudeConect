from django.urls import path
from . import views

app_name = 'locais'

urlpatterns = [
    path('', views.listar_locais, name='locais'),
    path('cadastrar/', views.criar_local, name='cadastrar_local'),
    path('<int:pk>/', views.detalhes_local, name='detalhes_local'),
    path('<int:pk>/editar/', views.editar_local, name='editar_local'),
    path('<int:pk>/excluir/', views.excluir_local, name='excluir_local'),
]