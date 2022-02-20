from django.urls import path
from App1_Blog_Coder import views

urlpatterns = [
    path('', views.inicio, name='app1_inicio'),
    path('pages/', views.pages, name='app1_pages'),
    path('about/', views.about, name='app1_about'),
    path('leer/', views.articulo, name='app1_articulo'),
    path('detail/', views.detail, name='app1_detail')
    
]