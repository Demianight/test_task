from django.contrib import admin

from recipes.models import Product, ProductAmount, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAmount)
class ProductAmountAdmin(admin.ModelAdmin):
    pass
