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
def sumPrices(d):
	total=0
	for k,v in d.iteritems(): 
		if k[:4]== 'item': 
			itemid=int(k[4:])
			price=MenuItem.objects.get(id=itemid).price
			print price,v
			total+=price*int(v)
	print total
	return total

@csrf_exempt
def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.menuitem_set.all()
	#for item in menuItems:
	#	print item.price
	print menuItems
	#print type (com)
	print type(menuItems)
	sumPrices(request.POST)
	#menu = MenuItem.objects.get(pk=price)
			#return HttpResponseRedirect(request.path) 
	
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'com':com, 'menuItems':menuItems})
	return HttpResponse(t.render(c))
@csrf_exempt
def displayView(request):
	total=sumPrices(request.POST)
	t=loader.get_template('MyFinalProject/confirm.html')
	c=Context({'total':total})
	return HttpResponse(t.render(c))
def restaurantView(request,id):
	order=Customer.objects.get(pk=id)
	order=order.order_set.all()
	t=loader.get_template('MyFinalProject/restaurant.html')
	c=Context(dict())
	return HttpResponse(t.render(c))

	
	
