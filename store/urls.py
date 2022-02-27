from django.urls import path
from . import views

urlpatterns = [
    # 1st augument is blank bc nothing comes after the store, Added for Hompage and remove default
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
]
