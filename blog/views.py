from django.shortcuts import render
from django.http import request


# import models.py (karena kita berhubungan dg DB dan kita ingin menampilkan data dr class 'Job')
from .models import Blog



# Create your views here.
# create views function for home page
def allblogs(request):
    
    #menampilkan obejct dr class 'Job' di models.py yg berisi data image dan summary
    blogs = Blog.objects
    
    
    return render(request, 'blog/allblogs.html', {'blogs':blogs})
