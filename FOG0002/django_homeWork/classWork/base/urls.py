from django.urls import path
from . import views

urlpatterns = [ 
    path('articles/', views.list_articles, name='list_articles'),  
    path('articles/create/', views.create_article, name='create_article'),
]
