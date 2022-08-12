from django.db import models

# Create your models here.

class UserDetails(models.Model):
	Fullname 	= models.CharField(max_length=200)
	Email 		= models.EmailField()
	Phone		= models.CharField(max_length=11)
	Address		= models.TextField()
	State 		= models.CharField(max_length=100)
	fufiled 	= models.BooleanField(default=False)
	product		= models.ForeignKey('products.Product', on_delete=models.CASCADE)