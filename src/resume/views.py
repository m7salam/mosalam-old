
from django.shortcuts import render
from projects.models import *
from blog.models import *
from .models import (
    Bio, 
    Job_Title, 
    Services, 
    Testimonial,
    Client,
    Education,
    Experience,
    Coding_Skill,
    Technology,

    )


def index(request):
    bio = Bio.objects.all()
    job_title = Job_Title.objects.all()
    service = Services.objects.all()
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    coding_skill = Coding_Skill.objects.all()
    technology = Technology.objects.all()
    project_featured = Project.objects.filter(featured=True)
    project = Project.objects.all()
    featured_blog = Post.objects.filter(featured=True)

    context = {
        "bio": bio,
        "job_title": job_title,
        "service": service,
        "testimonial" : testimonial,
        "client" : client,
        "education" : education,
        "experience" : experience,
        "coding_skill": coding_skill,
        "technology" : technology,
        "project_featured" : project_featured,
        "project": project,
        "featured_blog":featured_blog,






    }
    return render(request, 'index.html', context)
