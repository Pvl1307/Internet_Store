from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_product', 'price_of_product', 'category_of_product')
    list_filter = ('category_of_product', )
    search_fields = ('name_of_product', 'description_of_product')
