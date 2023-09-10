from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_product', 'price_of_product', 'category_of_product', 'user',)
    list_filter = ('category_of_product', 'user', )
    search_fields = ('name_of_product', 'description_of_product')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active')
    list_filter = ('product',)
    search_fields = ('version_number', 'version_name')
