# Generated by Django 2.2.3 on 2019-08-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190812_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
    ]