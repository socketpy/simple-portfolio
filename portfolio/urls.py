"""

ini adalah file global url path utk 'portpolio" project

"""

from django.conf.urls import url
from django.contrib import admin

# routing url pakek path, hrs import module ini
from django.urls import path, include

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
    path('', jobs.views.home, name='home'),
    
    # route to "blog" app (blog page)
    # dan yg dipakai adalah file "urls.py" di directory app "blog" bkn default global urls
    path('blog/', include('blog.urls')),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)