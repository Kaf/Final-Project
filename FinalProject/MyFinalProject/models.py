from django.db import models
from django.contrib import admin

class Company(models.Model):
	name=models.CharField(max_length=60)
	location=models.CharField(max_length=100)
	phoneNumber=models.IntegerField()
	def __unicode__(self):
		return self.name+","+str(self.location)
class MenuItem(models.Model):
	number=models.IntegerField(max_length=10)
	price=models.FloatField()
	item=models.CharField(max_length=20)
	companyId=models.ForeignKey(Company)
	def __unicode__(self):
		return str(self.item)+","+str(self.price)

class Customer(models.Model):
	phonenumber=models.IntegerField()
	def __unicode__(self):
		return str(self.phonenumber)
class Payment(models.Model):
	amount=models.FloatField()
	confirmationMessage=models.CharField(max_length=60)
	date=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return str(self.amount)+","+str(self.date)

class Order(models.Model):
	quantity=models.IntegerField()
	item=models.CharField(max_length=20)
        orderId=models.ForeignKey(Customer) 
	def __unicode__(self):
		return str(self.quantity)+","+self.item
class History(models.Model):
	OrderId =models.ForeignKey(Order)
	CustomerId=models.ForeignKey(Customer)
	total=models.FloatField()
	def __unicode__(self):
		return str(self.total)

class MenuItemInline(admin.TabularInline):
	model = MenuItem
class OrderInline(admin.TabularInline):
	model = Order
class HistoryInline(admin.TabularInline):
	model=History
class CustomerInline(admin.TabularInline):
	model=Customer


class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','location','phoneNumber')
	search_fields = ('name',)
	list_filter = ('name',)
	inlines = [MenuItemInline]

class MenuItemAdmin(admin.ModelAdmin):
	list_display=('number','price','item','companyId')
	list_filter = ('number','price')

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('phonenumber',)
	inlines = [OrderInline]
	inlines = [HistoryInline]

class PaymentAdmin(admin.ModelAdmin):
	list_display =('amount','confirmationMessage','date')
	search_fields = ('date',)
	
class OrderAdmin(admin.ModelAdmin):
	list_display = ('quantity','item')
	search_fields = ('item',)

class HistoryAdmin(admin.ModelAdmin):
	list_display =('OrderId','CustomerId','total')
	


admin.site.register(Company,CompanyAdmin)
admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(History,HistoryAdmin)
