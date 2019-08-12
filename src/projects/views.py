from django.shortcuts import render
from .models import Project,Images
from django.forms import modelformset_factory



def projects_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request,'projects/projects_index.html', context)


def projects_detail(request,slug):
    project = Project.objects.filter(slug=slug)
    context = {
        "project":project
    }
    
    return render(request,'projects/projects_detail.html', context)



