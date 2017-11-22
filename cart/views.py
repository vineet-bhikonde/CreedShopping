from django.shortcuts import render
from .models import CartItems
from products.models import Product_Details
from cart.form import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User_Orders
from random import randint

@login_required
def cart_view(request,product_id):
	if CartItems.objects.filter(pro_id=product_id).exists():
		ob=CartItems.objects.get(pro_id=product_id)
		ob.product_quantity=ob.product_quantity+1
		ob.save()
	else:
		p=Product_Details.objects.get(product_id=product_id)
		item=CartItems(pro_id=product_id,product_quantity=1,pro_name=p.product_name,pro_price=p.product_price)
		item.save()
	itm=CartItems.objects.raw('SELECT * FROM cart_cartitems;')
	total=0.0
	for i in itm:
		total=total+float(i.pro_price)*i.product_quantity
	print (total)
	if total==0.0:
		items_there=False
	else:
		items_there=True
	context={ 'items':itm , 'totalPrice':total,'items_there':items_there }
	template="shopping_cart.html"
	return render(request,template,context)

def cart(request):
	itm=CartItems.objects.raw('SELECT * FROM cart_cartitems;')
	total=0.0
	for i in itm:
		total=total+float(i.pro_price)*i.product_quantity	
	if total==0.0:
		items_there=False
	else:
		items_there=True
	context={'items':itm,'totalPrice':total,'items_there':items_there}
	template="shopping_cart.html"
	return render(request,template,context)


def checkout(request):
	if request.method =='POST':
		form=CheckoutForm(request.POST)
		if form.is_valid():
			ord_no=randint(50000,100000)
			username=request.user.username
			itm=CartItems.objects.raw('SELECT * FROM cart_cartitems;')
			total=0.0
			for i in itm:
				total=total+float(i.pro_price)*i.product_quantity
			User_Order=User_Orders(Order_No=ord_no,Username=username,total_price=total)
			User_Order.save()
			CartItems.objects.all().delete()
			return HttpResponseRedirect('/thanks/')
	form=CheckoutForm()
	return render(request,"checkout.html",{'form':form})