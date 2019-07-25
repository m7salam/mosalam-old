from django.shortcuts import render


def projects_index(request):
    return render(request,'projects_index.html', {})
