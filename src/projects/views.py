from django.shortcuts import render
from .models import Project


def projects_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,

    }
    return render(request,'projects/projects_index.html', context)


def projects_detail(request,slug, ajax_id="#projects"):
    project = Project.objects.filter(slug=slug)
    projects_id = Project.objects.filter(ajax_id=ajax_id)
    context = {
        "project": project,
        "id": projects_id,
    }
    
    return render(request,'projects/projects_detail.html', context)



