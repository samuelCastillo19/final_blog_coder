from django.urls import path
from App2_Login.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_request, name='app2_login'),
    path('register/', register, name='app2_register'),
    path('logout/', LogoutView.as_view(template_name='App2/logout.html'), name='app2_logout'),
    path('update_profile/', editar_perfil, name='app2_editar_perfil')
    
]