from django.db import models
from django.contrib import admin

class Company(models.Model):
	name = models.CharField(max_length=60)
	location = models.CharField(max_length=100)
	phoneNumber = models.IntegerField()
	def __unicode__(self):
		return self.name+","+str(self.location)

class MenuItem(models.Model):
	number = models.IntegerField(max_length=10)
	price = models.FloatField()
	name = models.CharField(max_length=100)
	company = models.ForeignKey(Company)
	def __unicode__(self):
		return str(self.company)+':   '+str(self.number)+"   "+str(self.name)+"    "+str(self.price)

#class Customer(models.Model):
#	phonenumber=models.IntegerField()
#	#history = models.ForeignKey(History)
#	def __unicode__(self):
#		return str(self.phonenumber)


class Order(models.Model):
	total=models.FloatField(blank=True,null=True)
	ispaid =  models.BooleanField()
	phonenumber = models.IntegerField(blank=True,null=True)
	placedorder = models.TextField()
	created     =  models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return str(self.total)+"  "+ str(self.phonenumber)


class Payment(models.Model):
	amount=models.FloatField()
	confirmationMessage=models.CharField(max_length=60)
	date=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return str(self.amount)+","+str(self.date)

class OrderItem(models.Model):
	Quant = (('1','1'),('2','2'))
	quantity= models.IntegerField(choices = Quant) 
	menuitem = models.ForeignKey(MenuItem)
	order = models.ForeignKey(Order)
	
	def __unicode__(self):
		return str(self.quantity)+","+str(self.menuitem)


class MenuItemInline(admin.TabularInline):
	model = MenuItem
	extra = 5
class OrderItemInline(admin.TabularInline):
	model = OrderItem
#class HistoryInline(admin.TabularInline):
#	model=History



class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','location','phoneNumber')
	search_fields = ('name',)
	list_filter = ('name',)
	inlines = [MenuItemInline]

class MenuItemAdmin(admin.ModelAdmin):
	list_display=('number','price','name','company')
	list_filter = ('number','price')

#class CustomerAdmin(admin.ModelAdmin):
#	list_display = ('phonenumber',)
#	inlines = [OrderItemInline]
#	inlines = [HistoryInline]

class OrderAdmin(admin.ModelAdmin):
	#list_display = ('menuitem','quantity','customer')
	list_filter = ('created',)
	inlines = [OrderItemInline]
	list_display = ('phonenumber','total','ispaid')


#class NumberOfItemAdmin(admin.ModelAdmin):
#	list_display = ('num',)

#class HistoryAdmin(admin.ModelAdmin):
#	list_display = ('CustomerId','total')

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('amount','date')
	search_fields = ('date',)

	
admin.site.register(Company,CompanyAdmin)
admin.site.register(MenuItem,MenuItemAdmin)
#admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment,PaymentAdmin)
#admin.site.register(History)#,HistoryAdmin)
#admin.site.register(NumberOfItem,NumberOfItemAdmin)
