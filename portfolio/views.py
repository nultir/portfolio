from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Project, Technologies
# Create your views here.


def home(request):
    projects = Project.objects.all()
    technologies = Technologies.objects.all()
    context = {
        'context': projects,
        'technologies': technologies
        }
    return render(request, 'portfolio/index.html', context)


def projects(request):
    template = loader.get_template('portfolio/projects.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('portfolio/contact.html')
    return HttpResponse(template.render())