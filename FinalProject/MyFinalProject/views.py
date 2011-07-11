# Create your views here.
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
#from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from models import Company, MenuItem,Customer,Payment,Order,History


def listView(request):
	getCompany=Company.objects.all()
	t = loader.get_template('MyFinalProject/companylist.html')
	c = Context({'getCompany':getCompany})
	return HttpResponse(t.render(c))
def home(request):
	t = loader.get_template('MyFinalProject/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))
def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.MenuItem_set.all()
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'com':com, 'MenuItems':MenuItems})
	return HttpResponse(t.render(c))
def displayView(request):
	t=loader.get_template('MyFinalProject/display.html')
	c=Context(dict())
	return HttpResponse(t.render(c))
def restaurantView(request,id):
	order=Customer.objects.get(pk=id)
	order=order.Order_set.all()
	t=loader.get_template('MyFinalProject/restaurant.html')
	c=Context(dict())
	return HttpResponse(t.render(c))

	
	
