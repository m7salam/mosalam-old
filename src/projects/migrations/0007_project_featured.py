# Generated by Django 2.2.3 on 2019-09-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_ajax_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
