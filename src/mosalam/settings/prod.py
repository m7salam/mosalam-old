from mosalam.settings.base import *


DEBUG = False
ALLOWED_HOSTS = ['mosalam.herokuapp.com',]



try:
    from mosalam.settings.local import *
except:
    pass