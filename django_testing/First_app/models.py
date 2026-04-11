
# Create your models here.

from django.db import models  
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name
    
    category = models.ManyToManyField(Category, related_name='products')