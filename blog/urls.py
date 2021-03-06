from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('all-articles', views.all_articles, name='all_articles'),
    path('<int:pk>/article-details', views.article_details, name='article_details'),
    path('search/', views.search, name='search'),
]

