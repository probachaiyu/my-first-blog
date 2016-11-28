from django.conf.urls import include, url, patterns
from django.contrib import admin
from registration.backends.simple.views import RegistrationView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),

    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #url(r'^accounts/register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
   

)