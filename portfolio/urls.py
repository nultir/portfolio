from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home1'),
    path('home', views.home, name='home2'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]

