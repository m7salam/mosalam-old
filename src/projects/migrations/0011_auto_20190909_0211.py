# Generated by Django 2.2.3 on 2019-09-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ManyToManyField(related_name='projects', to='projects.Images'),
        ),
    ]
