from django.db import models
from django.urls import reverse 
# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Project(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='Projects/')
    video = models.TextField(blank=True, null=True)
    technology = models.ManyToManyField('Technology', related_name='projects')
    category = models.ManyToManyField('Category', related_name='projects')
    website = models.CharField(max_length = 255, blank=True, null=True)
    ajax_id = models.CharField(max_length=255, default="#projects")
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'slug': self.slug})


class Images(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to = 'Projects/')

    def __str__(self):
        return self.project.title + "Images"
