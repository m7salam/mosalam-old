from .base import *


DEBUG = False
ALLOWED_HOSTS = ['mosalam.herokuapp.com',]

WSGI_APPLICATION = 'mosalam.wsgi.application'
sys.path.append

/app/src

try:
    from .local import *
except:
    pass