from django.contrib.auth import get_user_model
from django.db import models

from apps.packages.models import Package

User = get_user_model()


class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_carts',
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='package_carts',
    )

    quantity = models.PositiveSmallIntegerField(
        verbose_name="Количество",
    )
