from mosalam.settings.base import *


DEBUG = False
ALLOWED_HOSTS = ['mosalam.herokuapp.com',]

WSGI_APPLICATION = 'wsgi.application'

try:
    from mosalam.settings.local import *
except:
    pass