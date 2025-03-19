from django.shortcuts import render
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import *
from .serializers import *

# Create your views here.
def home(request):
    return render(request,"todo/index.html")




class CategoryView(APIView):

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class TaskView(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return TemplateResponse(request, 'todo/form.html', {'fields': serializer.fields})
    

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