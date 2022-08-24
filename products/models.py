from django.db import models

# Create your models here.
# Todo:
# make deals column
# make available column
# make category shop count, to be used to sort popularity
# add price, locatioin, brand, condition attribute in Product relation
# change fk from restrict to cascade
# add a review relation and add a foreign key in Product relation


class Product(models.Model):
	Name 		= models.CharField(max_length=200)
	image 		= models.ImageField(upload_to='images')  
	Description = models.TextField()
	category 	= models.ForeignKey(
							'Category',
							 on_delete=models.RESTRICT,

							 )

	def __str__(self):
		return self.Name

class Category(models.Model):
	category = models.CharField(max_length=100)


	def __str__(self):
		return self.category