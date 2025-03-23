from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home-todo'),
    path('category',views.CategoryView.as_view(), name='category'),
    path('task/',views.TaskView.as_view(), name='task'),
    path('category/',views.CategoryView.as_view(), name='category'),
    path('task/form/', views.TaskView_Form.as_view(), name='task-form'),
    path('category/form/', views.CategoryView_Form.as_view(), name='category-form'),
    
]

