from django.urls import path
from App1_Blog_Coder import views

urlpatterns = [
    path('', views.inicio, name='app1_inicio'),
    path('about/', views.about, name='app1_about'),
    path('pages/', views.ArticleListView.as_view(), name='app1_pages'),
    path('update_article/<pk>', views.ArticleUpdateView.as_view(), name='app1_update_article'),
    path('new_article/', views.ArticleCreateView.as_view(), name='app1_new_article'),
    path('delete_article/<pk>', views.ArticleDeleteView.as_view(), name='app1_delete_article'),
    path('detail_article/<pk>', views.ArticleDetailView.as_view(), name='app1_detail_article')
    
]