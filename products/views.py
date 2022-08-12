from django.shortcuts import render

# Create your views here.
def products_view(request):
	context = {

	}
	return render(request, 'products/products_view.html', context)


def products_detail_view(request):
	context = {

	}
	return render(request, 'products/products_detail_view.html', context)

