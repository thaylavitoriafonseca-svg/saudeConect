from django.urls import path

from vacinas import views

app_name = 'vacinas'
urlpatterns = [
# Vacinas
    path(
        '',
        views.VacinaListView.as_view(),
        name='vacinas'
    ),

    path(
        '<int:pk>/',
        views.VacinaDetailView.as_view(),
        name='vacina_detail'
    ),

    path(
        'cadastrar/',
        views.VacinaCreateView.as_view(),
        name='vacina_create'
    ),

    path(
        '<int:pk>/editar/',
        views.VacinaUpdateView.as_view(),
        name='vacina_update'
    ),

    path(
        '<int:pk>/excluir/',
        views.VacinaDeleteView.as_view(),
        name='vacina_delete'
    ),

]
