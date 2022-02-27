from re import T
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(
        max_length=50, unique=True)  # name of cat + max len +unique
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(
        upload_to='photos/categoriees', blank=True)  # blank is optional

    # To change django auto plural mispelling
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):  # need to pass self when in Class
        # will take the name of cat slug in store > urls.py and return url of cat
        return reverse('products_by_category', args=[self.slug])

    # String representation of model
    def __str__(self):
        return self.category_name
