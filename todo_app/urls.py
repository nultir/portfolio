from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('categories',views.CategoryView.as_view()),
    path('task',views.TaskView.as_view()),
    path('tasks/form/', views.FormView.as_view(), name='task-form'),
    
]

