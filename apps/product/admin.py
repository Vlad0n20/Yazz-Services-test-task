from django.contrib import admin

from apps.product.models import Product
from apps.product.forms import ProductForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['name', 'shop', 'price', 'weight']
    list_display_links = ['name']
    list_filter = ['shop', 'categories']
    search_fields = ['name', 'description', 'keywords']
