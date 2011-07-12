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
	for k,v in d.iter:
		if k[:4]== 'item':
			itemid=k[4]
			price=item.object.get(id=itemid)
			total+=price* POST[itemid]
	print total




def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.menuitem_set.all()
	for item in menuItems:
		print item.price
	print com,menuItems,od
	
	menu = MenuItem.objects.get(pk=id)
	if request.method == 'POST':
			return HttpResponseRedirect(request.path)
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'com':com, 'menuItems':menuItems})
	return HttpResponse(t.render(c))

def displayView(request):
	t=loader.get_template('MyFinalProject/confirm.html')
	c=Context(dict())
	return HttpResponse(t.render(c))

def restaurantView(request,id):
	order=Customer.objects.get(pk=id)
	order=order.order_set.all()
	t=loader.get_template('MyFinalProject/restaurant.html')
	c=Context(dict())
	return HttpResponse(t.render(c))


'''
class MenuForm(ModelForm):
    class Meta:
	exclude=['company']
	model = MenuItem
	
def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.menuitem_set.all()
	#menu = menuItems.objects.get(pk=id)
	if request.method == 'POST':
		form = MenuForm(request.POST)
		if form.is_valid():
			m = MenuItem.objects.filter(name__icontains=request.POST['price'])
			return HttpResponseRedirect(request.path)
	else:
        	form = MenuForm()
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'form':form.as_p(),'com':com, 'menuItems':menuItems})
	return HttpResponse(t.render(c))
	'''
