from django.urls import path

from campanhas import views

app_name = 'campanhas'
urlpatterns = [
# Campanhas
    path(
        '',
        views.campanhas,
        name='campanhas'
    ),

    path(
        'cadastrar/',
        views.CampanhaCreateView.as_view(),  # <-- Corrigido para a classe correta
        name='campanha_create'
    ),


]