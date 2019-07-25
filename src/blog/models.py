from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    creator = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    thumbnail = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.body
