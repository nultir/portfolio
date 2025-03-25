from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from .models import Project, Technologies
from .serializer import *
# Create your views here.


def home(request):
    projects = Project.objects.all()
    technologies = Technologies.objects.all()
    context = {
        'context': projects,
        'technologies': technologies
        }
    return render(request, 'portfolio/index.html', context)



class UserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("succes")
        return TemplateResponse(request, 'form.html', {'serializer': serializer,
                                                  'urls': 'user'})
    

class UserView_Form(APIView):
    
    def get(self,request):
        form = UserSerializer()
        return render(request, 'form.html', {'serializer': form,
                                                  'urls': 'user'})


