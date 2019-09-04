from django.shortcuts import render
from django.http import request


# import models.py (karena kita berhubungan dg DB dan kita ingin menampilkan data dr class 'Job')
from .models import Job



# Create your views here.
# create views function for home page
def home(request):
    
    #menampilkan obejct dr class 'Job' di models.py yg berisi data image dan summary
    jobs = Job.objects
    
    
    return render(request, 'jobs/home.html', {'jobs':jobs})
