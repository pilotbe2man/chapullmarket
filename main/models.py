import os
import random
import string
from django.db import models
from django.db.models import *
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address = models.CharField(max_length=120)

	def __unicode__(self):
		return u'%s %s' % (self.address)
		
class Offer(models.Model):
    item1 = models.ForeignKey('Item', related_name="item1")
    item2 = models.ForeignKey('Item', related_name="item2")
    status = models.CharField(max_length=10)
    class Meta:
        ordering = ('-id',)


def image_file_name(instance, filename):
	digits = "".join( [random.choice(string.digits) for i in xrange(6)] )
	return os.path.join('images', str(instance.has.id), digits+filename)


class Item(models.Model):

	OPEN = 'OPEN'
	RECYCLED = 'RECYCLED'
	CANCELED = 'CANCELED'

	STATE_CHOICES = (
        # the item will open.
        (OPEN, 'OPEN'),
   		# the item is recycled.
   		(RECYCLED, 'RECYCLED'),
        #
        (CANCELED, 'CANCELED'),
    )
	has = models.ForeignKey(User, related_name="Item")
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=120)
	usage_state = models.TextField(max_length=10)
	brand = models.CharField(max_length=50)
	status = models.CharField(max_length=10)
	astatus = models.CharField(max_length=20, choices=STATE_CHOICES, default=OPEN)
	photo = models.FileField(upload_to=image_file_name)

	def __unicode__(self):
		return u'%s %s %s %s %s' % (self.name, self.description, self.usage_state, self.brand, self.status)

	class Meta:
		ordering = ('-id',)
