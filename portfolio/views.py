from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
# Create your views here.


def home(request):
    template = loader.get_template('portfolio/home.html')
    return HttpResponse(template.render())


def projects(request):
    template = loader.get_template('portfolio/projects.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('portfolio/contact.html')
    return HttpResponse(template.render())