from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from users.user_form import * 
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import *
from cart.models import CartItems

def SignUp(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username,password=password)
			
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("/")
	form=UserForm()
	template="shopping_signup.html"
	return render(request,template,{'form':form})

def SignIn(request):
	if request.method=="POST":
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(request,username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					print(username)
					return redirect("/")
	form=SignInForm()
	template="shopping_signin.html"
	return render(request,template,{'form':form})

def Logout(request):
	CartItems.objects.all().delete()
	logout(request)
	return redirect("/signin")

def Orders(request):
	orders=User_Orders.objects.filter(Username=request.user.username)
	template="shopping_orders.html"
	return render(request,template,{'orders':orders})