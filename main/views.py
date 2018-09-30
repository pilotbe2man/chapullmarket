
from main.models import *
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import requires_csrf_token
from django.conf.urls.static import static
from django.views.decorators.debug import sensitive_post_parameters
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from main.forms import DocumentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
@csrf_exempt
def home(request):
	users = User.objects.all()
	
	itemx = list(Item.objects.all())
	if request.method == 'POST':
		#sign-in
		if "user_name" in request.POST and 'pass' in request.POST:
			username = request.POST.get('user_name')
			password = request.POST.get('pass')
			user = authenticate(username=username, password=password)
			if user:
				login(request,user)
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponseRedirect(reverse('home'))

	return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def sign_up(request):
	users = User.objects.all()
	if request.method == 'POST':
		# sign-up
		if "s_username" in request.POST and 's_pass' in request.POST and 's_passr' in request.POST and 'email' in request.POST:
			username = request.POST.get('s_username')
			password = request.POST.get('s_pass')
			passwordr = request.POST.get('s_passr')
			email = request.POST.get('email')

			if password == passwordr:
				try:
					User.objects.create_user(username, email, password)
					user = authenticate(username=username, password=password)
					login(request, user)
					return HttpResponseRedirect(reverse('home'))
				except:
					error_info="Error, please check inputs..."
					return render_to_response('sign_up.html', locals(), context_instance=RequestContext(request))

	return render_to_response('sign_up.html', locals(), context_instance=RequestContext(request))

@csrf_exempt
def profile(request, uname):
	users = User.objects.all()
	if request.user.is_authenticated:
		try:
			user = User.objects.get(username=uname)
		except:
			return HttpResponse("Error: user not existed!")
	else:

		return HttpResponseRedirect(reverse('home'))
 
	allitems = user.Item.all()

	return render_to_response('profile.html', locals(), context_instance=RequestContext(request))

def exit(request):
	logout(request)
	return HttpResponseRedirect('/')

@csrf_exempt
def additem(request):
	users = User.objects.all()
	items = Item.objects.all()
	form = DocumentForm()
	if request.method == 'POST':
		if "i_name" in request.POST and 'model' in request.POST and 'status' in request.POST and 'u_state' in request.POST and 'description' in request.POST:
			iname = request.POST.get('i_name')
			idesc = request.POST.get('description')
			iustate = request.POST.get('u_state')
			ibrand = request.POST.get('model')
			istat = request.POST.get('status')
			form = DocumentForm(request.POST, request.FILES)
			if form.is_valid():
				items = Item.objects.create(has= request.user, name = iname, description = idesc, usage_state = iustate, brand = ibrand, status = istat, photo = request.FILES['docfile'])
				error_info="Item has been added."
			else:
				form = DocumentForm()
				error_info="Error: Photo Type."
			return render_to_response('add_item.html', locals(), context_instance=RequestContext(request))
	return render_to_response('add_item.html', locals(),context_instance=RequestContext(request))

def listing(request):
	users = User.objects.all()
	items = Item.objects.all()
	paginator = Paginator(items, 15)
	page = request.GET.get('page')
	try:
		pagex = paginator.page(page)
	except PageNotAnInteger:

		pagex = paginator.page(1)
	except EmptyPage:

		pagex = paginator.page(paginator.num_pages)

	return render_to_response('list.html', locals(),context_instance=RequestContext(request))

	
def itemdetail(request, iid):
    users = User.objects.all()
  
    try:
        itemx = Item.objects.get(id=iid)
    except:
        return HttpResponse("Error: this item not existed!")

    return render_to_response('idetail.html', locals(), context_instance=RequestContext(request))

def search(request):
	users = User.objects.all()
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		items = Item.objects.filter(Q(name__contains=q) | Q(brand__contains=q) | Q(description__contains=q))
		return render_to_response('search_results.html', locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('home'))

@csrf_exempt
def recycle(request, uname, givenitemid):
	givenitem = givenitemid
	users = User.objects.all()
	if request.user.is_authenticated:
		try:
			user = User.objects.get(username=uname)
		except:
			return HttpResponse("Error: user not existed!")
	else:

		return HttpResponseRedirect(reverse('home'))
 
	allitems = user.Item.all()

	return render_to_response('recycle.html', locals(), context_instance=RequestContext(request))


def donerecycle(request, uiid, iid):
	users = User.objects.all()
	items = Item.objects.all()
	toitemid = uiid
	itemidto = iid
	item1x = Item.objects.get(id=toitemid) 
	item2x = Item.objects.get(id=itemidto)

	mewoffer = Offer.objects.create(item1 = item1x, item2 = item2x, status = 'offered')

	return render_to_response('successful.html', locals(),context_instance=RequestContext(request))

@csrf_exempt
def offers(request, uname):
	users = User.objects.all()
	if request.user.is_authenticated:
		try:
			user = User.objects.get(username=uname)
		except:
			return HttpResponse("Error: user not existed!")
	else:

		return HttpResponseRedirect(reverse('home'))
	allitems = Item.objects.all()
	alloffers = Offer.objects.all().filter(Q(item2__has=user) | Q(item1__has=user) )



	return render_to_response('offers.html', locals(), context_instance=RequestContext(request))

def agree(request, iid1, iid2, oid):
	users = User.objects.all()
	items = Item.objects.all()
	if request.user.is_authenticated:
		try:
			itemx1 = Item.objects.get(id=iid1)
			itemx1.astatus = 'RECYCLED'
			itemx1.save()

			itemx2 = Item.objects.get(id=iid2)
			itemx2.astatus = 'RECYCLED'
			itemx2.save()

			offerx = Offer.objects.get(id=oid)
			offerx.status = 'agree'
			offerx.save()

		except:
			return HttpResponse("Error: there is no such an item")
	return render_to_response('successful.html', locals(),context_instance=RequestContext(request))

def ignore(request, oid):
	users = User.objects.all()
	items = Item.objects.all()
	if request.user.is_authenticated:
		try:
			offerx = Offer.objects.get(id=oid)
			offerx.status = 'ignored'
			offerx.delete()
		except:
			return HttpResponse("Error: there is no such an item")
	return render_to_response('successful.html', locals(),context_instance=RequestContext(request))

def deleteitem(request, iid):
	users = User.objects.all()
	items = Item.objects.all()
	if request.user.is_authenticated:
		try:
			itemx = Item.objects.get(id=iid)
			itemx.delete()
		except:
			return HttpResponse("Error: there is no such an item")

	return render_to_response('successful.html', locals(),context_instance=RequestContext(request))
	
def aboutus(request):
	users = User.objects.all()
	return render_to_response('aboutus.html', locals(),context_instance=RequestContext(request))
