from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from recipes.models import Product, ProductAmount, Recipe


@api_view(['GET'])
def add_product_to_recipe(
    request: Request,
):
    param = request.query_params.get
    recipe_id = int(param('recipe_id'))
    product_id = int(param('product_id'))
    weight = int(param('weight'))

    if not Recipe.objects.filter(pk=recipe_id).exists():
        raise ValidationError('There is no such recipe')

    if not Product.objects.filter(pk=recipe_id).exists():
        raise ValidationError('There is no such product')

    if ProductAmount.objects.filter(
        product=product_id, recipe=recipe_id
    ).exists():
        prod_amount = ProductAmount.objects.get(
            product_id=product_id, recipe_id=recipe_id
        )
        prod_amount.weight = weight
    else:
        prod_amount = ProductAmount(
            recipe_id=recipe_id, product_id=product_id, weight=weight
        )

    prod_amount.save()

    return Response('Product successfully added to recipe')


@api_view(['GET'])
def cook_recipe(
        request: Request
):
    param = request.query_params.get
    recipe_id = int(param('recipe_id'))

    if not Recipe.objects.filter(pk=recipe_id).exists():
        raise ValidationError('There is no such recipe')

    for prod_amount in ProductAmount.objects.filter(recipe_id=recipe_id):
        product = Product.objects.get(pk=prod_amount.product.pk)
        product.incr_amount()
        product.save()

    return Response(
        ProductAmount
        .objects
        .filter(recipe_id=recipe_id)
        .values('product_id', 'product__cook_amount')
    )


def show_recipes_without_product(
        request: HttpRequest,
        product_id: int,
):
    recipes_without = Recipe.objects.exclude(amounts__product_id=product_id)
    recipes_with_lower_10 = Recipe.objects.filter(
        amounts__product_id=product_id,
        amounts__weight__lte=10
    )
    context = {
        'recipes_without': recipes_without,
        'recipes_with_lower_10': recipes_with_lower_10
    }
    return render(request, 'index.html', context)
