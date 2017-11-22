from django.shortcuts import render
from .models import Product_Details,Product_Categories
# Create your views here.
def home(request):
	products=Product_Details.objects.raw('SELECT * FROM products_product_details;')
	context={'pro':products}
	template='shopping_home.html'
	return render(request,template,context)

def about(request):
	template='shopping_about.html'
	context={}
	return render(request,template,context)

def contact(request):
	template='shopping_contact.html'
	context={}
	return render(request,template,context)

def thanks(request):
	template='shopping_thanks.html'
	context={}
	return render(request,template,context)

def mobile_details(request):
	items=Product_Details.objects.filter(cat_id=1)
	context={'pro':items,'cat':"MOBILE PRODUCTS"}
	template="product_details.html"
	return render(request,template,context)

def stationary_details(request):
	items=Product_Details.objects.filter(cat_id=2)
	context={'pro':items,'cat':"STATIONARY PRODUCTS"}
	template="product_details.html"
	return render(request,template,context)