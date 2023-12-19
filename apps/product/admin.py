from django.contrib import admin

from apps.product.models import Product, Category, ProductPhoto
from apps.product.forms import ProductForm


class ProductPhotoInline(admin.StackedInline):  # or use admin.TabularInline for a tabular layout
    model = ProductPhoto
    extra = 3
    fields = ['photo']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    inlines = [ProductPhotoInline]
    list_display = ['name', 'shop', 'price', 'weight']
    list_display_links = ['name']
    list_filter = ['shop', 'categories']
    search_fields = ['name', 'description', 'keywords']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'for_shop_type']
    list_display_links = ['name']
    list_filter = ['for_shop_type']
    search_fields = ['name']


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ['product', 'photo']
    list_display_links = ['product']
    search_fields = ['product']
