from django.contrib import admin

# Register your models here.


# import class 'Blog' di file 'models.py'
from .models import Blog


# kita coba menampilkan 'jobs app' yg kita buat
# utk menampilkan hrs lewat 'models' krn 'models' yg berhubungan dg DB utk ditampilkan di admin area
# class yg ada di 'models' ini hrs di register di admin site
admin.site.register(Blog)