from django.db import models

class User_Orders(models.Model):
	Order_No=models.CharField(max_length=10,primary_key=True)
	Username=models.CharField(max_length=15)
	total_price=models.DecimalField(decimal_places=2,max_digits=8)
