from django.shortcuts import render
from django.http import request

# Create your views here.


# create views function for home page
def home(request):
    return render(request, 'jobs/home.html')
