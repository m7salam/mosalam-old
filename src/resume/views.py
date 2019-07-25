
from django.shortcuts import render
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






    }
    return render(request, 'index.html', context)