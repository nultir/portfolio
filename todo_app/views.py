from django.shortcuts import render
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import datetime
from .models import *
from .serializers import *

# Create your views here.
def home(request):
    objects = {}
    
    if request.GET.get('date') != None:
        date = datetime.datetime.strptime(request.GET.get('date'),"%Y-%m-%d")
    else:
        date = objects['date'] = datetime.datetime.now()
    objects['date'] = date.strftime("%A %d %B %Y")
    tasks = Task.objects.filter(date_of_end__gte=date, date_of_start__lte=date)
    serializer = TaskSerializer(tasks,many=True)
    for x in serializer.data:
            x['category'] = Category.objects.filter(id=x['category']).first().name
    objects['tasks'] = serializer.data
    return TemplateResponse(request, 'todo/index.html', objects)
    




class CategoryView(APIView):

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return TemplateResponse(request, 'todo/list_category.html', {'objects': serializer.data})
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return TemplateResponse(request, 'todo/list_category.html', {'objects': [serializer.data]})
        return TemplateResponse(request, 'todo/form.html', {'fields': serializer.data})
    

class TaskView(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        for x in serializer.data:
            x['category'] = Category.objects.filter(id=x['category']).first().name
        return TemplateResponse(request, 'todo/list_task.html', {'objects': serializer.data})
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return TemplateResponse(request, 'todo/list_task.html', {'objects': [serializer.data]})
        return TemplateResponse(request, 'todo/form.html', {'fields': serializer.data})
    

class TaskView_Form(APIView):
    def get(self,request):
        form = TaskSerializer()
        return render(request, 'todo/form.html', {'serializer': form,
                                                  'urls': 'task'})
    

class CategoryView_Form(APIView):
    def get(self,request):
        form = CategorySerializer()
        return render(request, 'todo/form.html', {'serializer': form,
                                                  'urls': 'category'})