from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse('index page')

def hello(request, username):
    return HttpResponse('<h2>Hello %s </h2>' % username)

def projects(request):
    projects = list(Project.objects.values())  
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    get_object_or_404(task, id=id)
    return HttpResponse('tasks: %s' % task.title)