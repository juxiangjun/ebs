import os, sys
import django.core.handlers.wsgi
path = os.path.dirname(__file__)
sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'sas.settings'
application = django.core.handlers.wsgi.WSGIHandler()
