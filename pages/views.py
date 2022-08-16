from django.shortcuts import render
from products.models import Product, Category
import requests

# Create your views here.
def index_view(request):
	# r = requests.get('https://fakestoreapi.com/products')

	# for item in r.json():
	# 	try:
	# 		category_name = Category.objects.get(category=item['category'])
	# 	except:
	# 		category_name = Category(category=item['category'])
	# 		category_name.save()
	# 	product = Product(
	# 		Name=item['title'], 
	# 		image=item['image'], 
	# 		Description=item['description'], 
	# 		category=category_name
	# 		)
	# 	product.save()
	all_categories = Category.objects.all()
	nine_products = Product.objects.all()[:9]

	context = {

		'all_categories': all_categories,
		'nine_products' : nine_products,

	}
	return render(request, 'index.html', context)

def about_view(request):
	context = {
	
	}
	return render(request, 'about_view.html', context)


def contact_view(request):
	context = {
	
	}
	return render(request, 'contact_view.html', context)

def load_into_db(request):
	r = requests.get('https://fakestoreapi.com/products')
	print(r.text)
	context = {
	
	}
	return render(request, 'contact_view.html', context)