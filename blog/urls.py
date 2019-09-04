"""

ini adalah file custom url path utk applikasi 'blog"

"""


# routing url pakek path, hrs import module ini
from django.urls import path, include
from . import views



urlpatterns = [
    
    # default index page for app 'job'
    path('', views.allblogs, name='allblogs'),
     
]