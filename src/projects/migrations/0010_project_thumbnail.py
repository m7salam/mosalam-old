# Generated by Django 2.2.3 on 2019-09-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20190908_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Thumbnail/'),
        ),
    ]
