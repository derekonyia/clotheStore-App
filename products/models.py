from django.db import models

# Create your models here.
# Todo:
# make deals column
# make available column
# make category shop count, to be used to sort popularity

class Product(models.Model):
	Name 		= models.CharField(max_length=100)
	image 		= models.ImageField(upload_to='images')  
	Description = models.TextField()
	category 	= models.ForeignKey(
							'Category',
							 on_delete=models.RESTRICT,

							 )

class Category(models.Model):
	category = models.CharField(max_length=10)

# # populates the Category table with known categories from known_categories list
# 	def populate_category(self, *args, **kwargs):
# 		known_categories = ['Bedsheet', 'pillowcases', 'duvet']
# 		if self.objects.all() == none:
# 			for category in known_categories:
# 				self.objects.create(category=category)
# 		return True 
