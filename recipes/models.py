from django.db import models


class Recipe(models.Model):
    name = models.CharField(
        max_length=128,
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(
        max_length=128,
    )
    cook_amount = models.PositiveSmallIntegerField(default=0)

    def incr_amount(self):
        self.cook_amount += 1

    def __str__(self) -> str:
        return f'{self.name}'


class ProductAmount(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='amounts'
    )
    weight = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.product.name} in {self.recipe.name}'
