from django.db import models

# Create your models here.
class Product_Categories(models.Model):
	cat_id=models.DecimalField(decimal_places=0,max_digits=4,unique=True)
	cat_name=models.CharField(max_length=20)

	def __str__(self):
		return self.cat_name

class Product_Details(models.Model):
	product_id=models.DecimalField(decimal_places=0,max_digits=4,unique=True)
	product_image=models.TextField(max_length=100)
	product_name=models.CharField(max_length=20)
	product_desc=models.TextField(max_length=100)
	product_price=models.DecimalField(decimal_places=2,max_digits=8)
	cat_id=models.ForeignKey(Product_Categories)

	def __str__(self):
		return self.product_name
