"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# routing url pakek path, hrs import module ini
from django.urls import path

#import settings.py
from django.conf import settings

# import static
from django.conf.urls.static import static

# import views.py yg kita pakai, yaitu di direktory app jobs
import jobs.views



urlpatterns = [
    
    # page admin panel
    url(r'^admin/', admin.site.urls),
    
    # page home
    path('', jobs.views.home, name='home')
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)