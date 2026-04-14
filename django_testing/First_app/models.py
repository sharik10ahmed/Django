from django.db import models

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.category_name


# Product Model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name
