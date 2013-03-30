from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^showLoginForm', 'user.views.showLoginForm'),
    url(r'^login', 'user.views.login'),
)
