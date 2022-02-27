from django.contrib import admin
from .models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):  # Class for auto slug generation
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


# Registering classes
admin.site.register(Category, CategoryAdmin)
