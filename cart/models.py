from django.db import models
import products

class CartItems(models.Model):
	pro_id=models.DecimalField(max_digits=4,decimal_places=0,primary_key=True)
	pro_name=models.CharField(max_length=20)
	product_quantity=models.IntegerField(default=0)
	pro_price=models.DecimalField(decimal_places=2,max_digits=8)


