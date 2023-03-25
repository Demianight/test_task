from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128, unique=True,)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
