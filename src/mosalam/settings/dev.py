from mosalam.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1']


try:
    from mosalam.settings.local import *
except:
    pass
