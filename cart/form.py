from django import forms

class CheckoutForm(forms.Form):
	Name=forms.CharField(max_length=25)
	address=forms.CharField(max_length=50)
	card_holder_name=forms.CharField(max_length=25)
	card_num=forms.CharField(max_length=19)
	card_expiry=forms.CharField(max_length=5)
	card_cvv=forms.CharField(max_length=3,widget=forms.PasswordInput)
	
