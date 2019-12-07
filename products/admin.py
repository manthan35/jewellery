from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type','is_published', 'price', 'list_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    list_per_page = 25  

admin.site.register(Product,ProductAdmin)