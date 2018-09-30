from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = patterns(
	'',
	url(r'^$', 'main.views.home', name='home'),
	url(r'^logout/', 'main.views.exit', name='logout'),
	url(r'^sign_up/$', sign_up),
	url(r'^profile/([^/]+)/$', 'main.views.profile', name='profile'),
	url(r'^offers/([^/]+)/$', 'main.views.offers', name='offers'),
	url(r'^recycle/([^/]+)/([^/]+)/$', 'main.views.recycle', name='recycle'),
	url(r'^donerecycle/([^/]+)/([^/]+)/$', 'main.views.donerecycle', name='donerecycle'),
	url(r'^additem/$', 'main.views.additem', name='additem'),
	url(r'^agree/([^/]+)/([^/]+)/([^/]+)/$', 'main.views.agree', name='agree'),
	url(r'^ignore/([^/]+)/$', 'main.views.ignore', name='ignore'),
	url(r'^items/$', listing),
	url(r'^aboutus/$', aboutus),
	url(r'^listing/$', listing),
	url(r'^itemdetail/([^/]+)/$', 'main.views.itemdetail', name='itemdetail'),
	url(r'^search/$', search),
)+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
