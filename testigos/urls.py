from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cargar-municipios/', cargar_municipios, name='cargar_municipios'),
    path('cargar-comunas/', cargar_comunas, name='cargar_comunas'),
    path('cargar-candidatos/', cargar_candidatos, name='cargar_candidatos'),
    path('cargar-zonas/', cargar_zonas, name='cargar_zonas'),
    path('cargar-puestos/', cargar_puestos, name='cargar_puestos'),
    path('cargar-mesas/', cargar_mesas, name='cargar_mesas'),

    path('login/', user_login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login/index.html'),name='logout'),


    path('testigos/', Testigos.as_view(), name='testigos'),
    path('data/', data, name='data'),
    path('guardar-testigo/', guardar_testico_mesa, name='guardar-testigo'),
    # path('user/',UserView.as_view(), name='user_list'),
    # path('activar/<uidb64>/<token>/', activar_cuenta, name='activar_cuenta'),
    # # path('enviar/', enviar_email_activacion, name='enviar_cuenta'),
    # path('accounts/password/change/first-login/', FirstLoginPasswordChangeView.as_view(), name='password_change_first_login'),
    # path('subir-csv/', subir_csv, name='subir_csv'),
    # path('votar/', votar, name='votar'),
    # path('resultado/', resultado, name='resultado'),
]
