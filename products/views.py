from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def products_view(request):
	context = {

	}
	return render(request, 'products/products_view.html', context)


def product_detail_view(request, id):
	product = Product.objects.get(pk=id)
	context = {
		'product': product
	}
	return render(request, 'products/product_detail_view.html', context)


def add_to_session(request, id):
	# add product to session after 'add to cart' button is clicked
	item = Product.objects.get(pk=id)
	if 'cart' in request.session:
		if id in request.session['cart']:
			pass
		else:
			request.session['cart'].append(id)
	else:
		request.session['cart'] = [id]

	request.session.modified = True
	print(f'items {request.session["cart"]}')
	return redirect('product detail view', id=id)

def cart_view(request):
	items = []
	if 'cart' in request.session:
		cart = request.session['cart']
		for num in cart:
			product = Product.objects.get(pk=num)
			items.append(product)
	context = {
		'items' : items
	}
	return render(request, 'products/cart_view.html', context)