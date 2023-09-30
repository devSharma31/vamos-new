from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=500, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/", default="")  # Requires Pillow library for image fields

    def __str__(self):
        return self.product_name
   

   