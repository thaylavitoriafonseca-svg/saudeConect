from django.urls import path

from campanhas import views

app_name = 'campanhas'
urlpatterns = [
    path('', views.campanhas, name='campanhas'),
    path('cadastrar/', views.CampanhaCreateView.as_view(), name='campanha_create'),
    path('<int:pk>/', views.CampanhaDetailView.as_view(), name='campanha_detail'),
    path('<int:pk>/editar/', views.CampanhaUpdateView.as_view(), name='campanha_update'),
    path('<int:pk>/excluir/', views.CampanhaDeleteView.as_view(), name='campanha_delete'),
]
