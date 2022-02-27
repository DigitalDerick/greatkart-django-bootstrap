from audioop import reverse
from django.db import models
from category.models import Category
from django.urls import reverse  # Import reverse

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    # When category is deleted so are prods
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE)

    # When category is delete prods are kept but not related
    category = models.ForeignKey(  # ForeightKey interconnects classes
        Category, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        # returns the name of the path in urls.py and slugs
        return reverse('product_detail', args=[self.category.slug, self.slug])

    # String representation of model
    def __str__(self):
        return self.product_name
