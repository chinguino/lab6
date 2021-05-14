from django.shortcuts import render

# Create your views here.
#  hello/views.py

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'website/home.html')

def contact_page_view(request):
	return render(request, 'website/contact.html')

def info_page_view(request):
	return render(request, 'website/info.html')

def base_page_view(request):
	return render(request, 'website/base.html')
