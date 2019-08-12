from django.urls import path
from . import views


app_name = 'projects'


urlpatterns = [
    path("", views.projects_index, name="projects_index"),
    path("<slug:slug>/", views.projects_detail, name="projects_detail"),

]
