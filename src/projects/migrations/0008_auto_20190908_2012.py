# Generated by Django 2.2.3 on 2019-09-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ajax_id',
            field=models.CharField(default='general', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Projects/'),
        ),
    ]