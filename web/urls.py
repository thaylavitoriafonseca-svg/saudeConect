from django.urls import path

from web import views

app_name = 'web'
urlpatterns = [
# Página inicial
    path(
        '',
        views.home,
        name='home'
    ),
]