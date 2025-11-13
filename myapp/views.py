from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'Django curso!'
    return render(request, 'index.html',{
        'titulo': title
    })
    

def about(request):
    username = 'fazt'
    return render(request, 'about.html',{
        'username':username
    })

def hello(request, username):
    return HttpResponse('<h2>Hello %s </h2>' % username)

def projects(request):
    #projects = list(Project.objects.values())  
    projects=Project.objects.all()
    return render(request, 'projects.html',{
        'proyectos':projects
    })

def tasks(request):
    # get_object_or_404(task, id=id)
    return render(request, 'tasks.html')