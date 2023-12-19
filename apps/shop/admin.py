from django.contrib import admin

from apps.shop.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'latitude', 'longitude', 'sales_commission']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['type']
