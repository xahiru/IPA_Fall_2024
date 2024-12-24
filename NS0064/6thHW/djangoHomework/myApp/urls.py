from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.helloWorld, name="helloWorld"),
    path('blog/', views.blog, name ='blog'),
]