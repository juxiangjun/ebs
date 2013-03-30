from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sas.views.home', name='home'),
    url(r'^user/', include('user.urls')),
    url(r'^stock/', include('stock.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
