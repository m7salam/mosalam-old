# Generated by Django 2.2.3 on 2019-09-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190721_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
