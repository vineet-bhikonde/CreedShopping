from django.contrib import admin
from .models import Product_Details,Product_Categories
# Register your models here.

class Product_DetailsAdmin(admin.ModelAdmin):
	list_display=["product_id","product_name","cat_id"]
	list_display_links=['product_name']
	list_filter=['product_price']
	class Meta:
		model=Product_Details

	def __str__(self):
		return self.product_name

class Product_CategoriesAdmin(admin.ModelAdmin):
	list_display=["cat_id","cat_name"]
	list_display_links=['cat_name']
	class Meta:
		model=Product_Categories

	def __str__(self):
		return self.cat_name

admin.site.register(Product_Details,Product_DetailsAdmin)

admin.site.register(Product_Categories,Product_CategoriesAdmin)	
