from django.conf.urls import url, patterns, include
from . import views
from django.contrib import auth 



urlpatterns = [
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
   
 ]