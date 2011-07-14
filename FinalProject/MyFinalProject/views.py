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


#Create neworder
#totalprice=0
#for each posted menuitem where qty>0:
#	create orderitem
#	get price of menuitem
 #       totalprice = totalprice + qty*menuitemprice
#end for
#neworder.price = totalprice
#neworder.save
	
'''def sumPrices(d):
	tot=0
        total=0
	telNumber = ' '
	orderedfood= ' '
	for k,v in d.iteritems(): 
		if k[:4]== 'item': 
			itemid=int(k[4:])
			price=MenuItem.objects.get(id=itemid).price
			 
			print price,v
			tot+=price*int(v)
			if int(v) !=0:
				orderedfood += 	str(MenuItem.objects.get(id=itemid).number)+" "+str(MenuItem.objects.get(id=itemid).name)+" " + v +"\n"	
		if k[:3]=='tel':
			telNumber+=v
        total+=(tot*0.05)+tot		
	print tot,total,telNumber
	return total,telNumber,orderedfood '''

@csrf_exempt
def menuView(request, id):
	com=Company.objects.get(pk=id)
	menuItems = com.menuitem_set.all()
	#for item in menuItems:
	#	print item.price
	print menuItems
	#print type (com)
	print type(menuItems)
	#menu = MenuItem.objects.get(pk=price)
			#return HttpResponseRedirect(request.path) 
	
	t = loader.get_template('MyFinalProject/menulist.html')
	c = Context({'Company':Company,'com':com, 'menuItems':menuItems})
	return HttpResponse(t.render(c))

#Create neworder
#totalprice=0
#for each postvariable:
#	if contains "item" and qty>0
#		get menuitem
#		create orderitem
#		get price of menuitem
 #       	totalprice = totalprice + qty*menuitemprice
#end for
#neworder.price = totalprice
#neworder.save
@csrf_exempt
def displayView(request):
	newOrder = Order.objects.create(phonenumber=request.POST['tel'])
	totalprice = 0
	orderedfood= ' '
	print request.POST
	for k,v in request.POST.iteritems():
		if k[:4]== 'item' and int(v)>0: 
			itemid=int(k[4:])
			mi=MenuItem.objects.get(id=itemid)
			newOrderItem = OrderItem.objects.create(order=newOrder, menuitem=mi, quantity=int(v))
                	totalprice += int(v)*mi.price
			#orderedfood += 	"menu number:  "+str(MenuItem.objects.get(id=itemid).number)+"    "+ "item Name   :"+  str(MenuItem.objects.get(id=itemid).name)+"   " +" Price   " + v +"\n"	
			orderedfood += 	str(MenuItem.objects.get(id=itemid).number)+".   "+ "Item:"+  str(MenuItem.objects.get(id=itemid).name)+"   " +"quantity  " + v +"\n"	
	#newOrderItem = OrderItem.objects.create(order=newOrder, menuItem=mi)
	newOrder.total=totalprice
	newOrder.placedorder = orderedfood
	newOrder.save()
	t=loader.get_template('MyFinalProject/confirm.html')
	c=Context({'totalprice':totalprice})
	return HttpResponse(t.render(c))



def restaurantView(request):
	#order=order.order_set.all().filter()
	#print order
	orders = Order.objects.all().order_by('-created')
	for order in orders:
		order.placedorder = order.placedorder.split('\n')[:-1]		
	t = loader.get_template('MyFinalProject/restaurant.html')
	c = Context({'orders':orders})
	return HttpResponse(t.render(c))
	#customer=Customer.objects.get(order.customer)
	#telNumber = customer.phonenumber	



#try:
#	phonenumber = regex
#except:(KeyError,....)
#	return something.
