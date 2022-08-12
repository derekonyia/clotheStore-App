from django.shortcuts import render

# Create your views here.
def index_view(request):
	context = {

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