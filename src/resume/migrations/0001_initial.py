# Generated by Django 2.2.3 on 2019-07-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('bio_body', models.TextField()),
            ],
        ),
    ]
