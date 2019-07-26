from .base import *


DEBUG = False
ALLOWED_HOSTS = ['mosalam.herokuapp.com',]

WSGI_APPLICATION = 'mosalam.wsgi'

try:
    from .local import *
except:
    pass