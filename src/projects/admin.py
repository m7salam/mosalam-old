from django.contrib import admin
from .models import Technology, Project, Category, Images
# Register your models here.


admin.site.register(Technology)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Images)
