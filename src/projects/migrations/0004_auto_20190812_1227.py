# Generated by Django 2.2.3 on 2019-08-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190812_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(related_name='projects', to='projects.Category'),
        ),
    ]
