
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from usuarios.forms import EmailAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Aplicativos do projeto
    path('campanhas/', include('campanhas.urls')),
    path('locais/', include('locais.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('vacinas/', include('vacinas.urls')),

    # Página inicial
    path('', include('web.urls')),

    # Login
    path(
        'login/',
        LoginView.as_view(
            template_name='usuario/acesso/login.html',
            authentication_form=EmailAuthenticationForm,
            redirect_authenticated_user=True,
            next_page='web:home',
        ),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        LogoutView.as_view(next_page='login'),
        name='logout'
    ),
]
