"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


from mywebsite.settings import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import *

from vege.views import *

urlpatterns = [
    path('' , home ),

    path('contact/' , contact ),

    path('about/' , about ),


    path('login/' , login_page ),
    path('register/' , register ),

    path('logout/' , logout_page ),
    
    path('success_page/' , success_page),

    path('receipes' , receipes),

    path('delete_receipes/<id>/' , delete_receipes),

    path('update_receipes/<id>/' , update_receipes),

    path('students/' , get_students),

    path('see_marks/<student_id>' , see_marks),

    path('send_email' , send_email, name= "send_email" ),


    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()