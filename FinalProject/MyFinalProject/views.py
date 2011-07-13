# Create your views here.
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
#from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from models import Company, MenuItem,Payment,Order,OrderItem


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
	tot=0
        total=0
	telNumber = ' '
	for k,v in d.iteritems(): 
		if k[:4]== 'item': 
			itemid=int(k[4:])
			price=MenuItem.objects.get(id=itemid).price
			print price,v
			tot+=price*int(v)		
		if k[:3]=='tel':
			telNumber+=v
        total+=(tot*0.05)+tot		
	print tot,total,telNumber
	return total,telNumber
'''
@csrf_exempt
def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.menuitem_set.all()
	#for item in menuItems:
	#	print item.price
	print menuItems
	#print type (com)
	print type(menuItems)
	total = sumPrices(request.POST)
	#menu = MenuItem.objects.get(pk=price)
			#return HttpResponseRedirect(request.path) 
	
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'com':com, 'menuItems':menuItems})
	return HttpResponse(t.render(c))
'''

@csrf_exempt
def displayView(request):
	totalList=sumPrices(request.POST)
	total = totalList[0]
	telNum = totalList[1]
	print telNum
	t=loader.get_template('MyFinalProject/confirm.html')
	c=Context({'total':total})
	return HttpResponse(t.render(c))



def restaurantView(request,order_id):
	#order=order.order_set.all().filter()
	#print order
	order = Order.objects.get(pk=order_id)
	#customer=Customer.objects.get(order.customer)
	#telNumber = customer.phonenumber	
	t=loader.get_template('MyFinalProject/restaurant.html')
	c=Context({'telNumber':telNumber})
	return HttpResponse(t.render(c))


class OrderForm(ModelForm):
    class Meta:
	exclude=['ispaid']
	model = Order
	



#class OrderItemForm(ModelForm):
 #   class Meta:
#	exclude=['menitem']
#	model = OrderItem

	
def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.menuitem_set.all()
	#orderitem = OrderItem.objects.select_related().get(id=phonenumber)
	#quant = orderitem.quantity
	#menu = menuItems.objects.get(pk=id)
	for e in OrderItem.objects.all():
    		print e.quantity
	if request.method == 'POST':
		form = OrderForm(request.POST)
		#form1 = OrderItemForm(request.POST)
		if form.is_valid() and form1.is_valid():
			form.save()
		#	form1.save()
			#m = menuItems.objects.filter(name__icontains=request.POST['price'])
			print menuItems
			return HttpResponseRedirect(request.path)
	else:
        	form = OrderForm()
		#form1 = OrderItemForm
		
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'form':form.as_p(),#'quant':quant,#'form1':form1.as_p(),
	'com':com,'menuItems':menuItems})
	return HttpResponse(t.render(c))
'''
def getphonenum(d):
	telNumber = ' '
	for k,v in d.iteritems(): 
		if k[:3]=='tel':
			telNumber+=v
        #print tot,total,telNumber
	return telNumber
	'''
