# Generated by Django 2.2.4 on 2019-09-01 05:44
"""
Kalau berhasil create model utk create fields/table di DB akan generate filey 0001_initial.py ini
"""
from django.db import migrations, models

from PIL import Image

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            # nama table = job
            name='Job',

            #nama fields dalam table 'job'
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]