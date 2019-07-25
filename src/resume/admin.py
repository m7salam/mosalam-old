from django.contrib import admin
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




admin.site.register(Bio)
admin.site.register(Job_Title)
admin.site.register(Services)
admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Coding_Skill)
admin.site.register(Technology)



