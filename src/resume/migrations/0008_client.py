# Generated by Django 2.2.3 on 2019-07-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20190724_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(upload_to='client/')),
                ('link', models.TextField(blank=True, default='#', null=True)),
            ],
        ),
    ]
