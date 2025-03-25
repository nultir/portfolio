from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home1'),
    path('home', views.home, name='home2'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/logo.png'))),
    path('user_view', views.UserView.as_view(), name='user'),
    path('registration', views.UserView_Form.as_view(), name='user_form'),

]

