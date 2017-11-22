from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	passowrd=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','email','password']

class SignInForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		fields=['username','password']