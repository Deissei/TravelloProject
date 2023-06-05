from django.contrib.auth import get_user_model
from django.db import models

from apps.packages.models import Package

User = get_user_model()


class CartItem(models.Model):
    def subtotal(self, quantity:int, price:int):
        return quantity * price
    
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

    @property
    def total_price(self):
        return self.subtotal(self.quantity, self.package.price_per_person)


