

class Company(models.Model):
	Name=models.CharField(max_length=60)
	Location=models.charField(max_length=100)
	PhoneNumber=models.IntegerField()


class Customer(models.Model):
	Phone Number=models.IntergerField()

class Order(models.Model):
	Quantity=models.IntegerField()
	Item=models.CharField(max_length=20)
        OrderId=models.ForeignKey(Customer) 

class CommentInline(admin.TabularInline):
	model = Comment
