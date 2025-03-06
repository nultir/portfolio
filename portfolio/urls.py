from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home1'),
    path('home', views.home, name='home2'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/logo.png')))
]

