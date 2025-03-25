from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import datetime
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    objects = {}
    if request.GET.get('date') != None:
        date = datetime.datetime.strptime(request.GET.get('date'),"%Y-%m-%d")
    else:
        date = objects['date'] = datetime.datetime.now()
    objects['date'] = date.strftime("%A %d %B %Y")
    tasks = Task.objects.filter(date_of_end__gte=date, date_of_start__lte=date, person_id=request.user )
    serializer = TaskSerializer(tasks,many=True)
    for x in serializer.data:
            x['category'] = Category.objects.filter(id=x['category']).first().name
    objects['tasks'] = serializer.data
    return TemplateResponse(request, 'todo/index.html', objects)
    




class CategoryView(APIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        categories = Category.objects.filter(person_id=request.user).values()
        serializer = CategorySerializer(categories, many=True)
        return TemplateResponse(request, 'todo/list_category.html', {'objects': serializer.data})

    def post(self, request, format=None):
        data = request.data.copy()
        data['person'] = request.user.id
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return TemplateResponse(request, 'todo/list_category.html', {'objects': [serializer.data]})
        return TemplateResponse(request, 'form.html', {'fields': serializer.data})
    

class TaskView(APIView,LoginRequiredMixin):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        tasks = Task.objects.filter(person_id=request.user).values()
        serializer = TaskSerializer(tasks,many=True)
        for x in serializer.data:
            x['category'] = Category.objects.filter(id=x['category']).first().name
        return TemplateResponse(request, 'todo/list_task.html', {'objects': serializer.data})

    def post(self, request, format=None):
        data = request.data.copy()
        data['person'] = request.user.id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return TemplateResponse(request, 'todo/list_task.html', {'objects': [serializer.data]})
        return TemplateResponse(request, 'form.html', {'fields': serializer.data})
    

class TaskView_Form(APIView,LoginRequiredMixin):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        form = TaskSerializer()
        form.fields.pop('person')
        return render(request, 'form.html', {'serializer': form,
                                                  'urls': 'task'})
    

class CategoryView_Form(APIView,LoginRequiredMixin):
    
    def get(self,request):
        form = CategorySerializer()
        form.fields.pop('person')
        return render(request, 'form.html', {'serializer': form,
                                                  'urls': 'category'})