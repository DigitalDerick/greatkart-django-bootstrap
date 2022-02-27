from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from . models import Product  # .models as we have the models in the same app
from category.models import Category
# Create your views here.


def store(request, category_slug=None):
    # prods are available in templates > store > store.html
    categories = None
    products = None
    if category_slug != None:
        # Referring to category app > models.py
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)  # Will pull all products that are in the above cats
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {  # passing dict and values to html page
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)  # renders store view


def product_detail(request, category_slug, product_slug):  # passing in slugs + request
    try:
        # __ is the syntax to have access to slug of model
        # setting cat/prod slugs to single prod
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {  # passing dict and values to html page
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
