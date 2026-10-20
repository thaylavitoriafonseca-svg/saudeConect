from django.urls import path

from locais import views

app_name = 'locais'

urlpatterns = [
path(
        '',
        views.locais,
        name='locais'
    ),
]