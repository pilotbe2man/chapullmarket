import os
import sys
import socket
#import locale
#locale.setlocale(locale.LC_ALL, ('tr_TR', 'UTF-8'))
reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['LANG']='tr_TR.UTF-8'
os.environ['LC_ALL']='tr_TR.UTF-8'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chapullmarket.settings")
# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
sys.path.append('/home/chapullmarket/chapullmarket')
sys.path.append('/home/chapullmarket/chapullmarket/lib/python2.7/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chapullmarket.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
