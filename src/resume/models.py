from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=255)
    bio_body = models.TextField()

    def __str__(self):
        return self.name

class Job_Title(models.Model):
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return self.job_title

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank = True)
    icon = models.TextField(null=True, blank = True,default='example of css class: <i class="lnr lnr-laptop-phone"></i> ')

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    person = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    body = models.TextField()
    picture = models.ImageField(upload_to='Testimonial/')

    def __str__(self):
        return self.person
    

class Client(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='client/')
    link = models.TextField(default='#', null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    university = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    overview = models.TextField(default='', null=True, blank=True)


    def __str__(self):
        return self.university


class Experience(models.Model):
    job = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    overview = models.TextField(default='', null=True, blank=True)


    def __str__(self):
        return self.job + ' ' + 'in' + ' ' + self.company


class Coding_Skill(models.Model):
    skill = models.CharField(max_length=255)
    level = models.CharField(max_length=255, default = '95%')
    style_class = models.TextField(default='skill-percentage skill-1')



    def __str__(self):
        return self.skill


class Technology(models.Model):
    technology = models.CharField(max_length=255)
    level = models.CharField(max_length=255, default = '95%')
    style_class = models.TextField(default='skill-percentage skill-5')


    def __str__(self):
        return self.technology
