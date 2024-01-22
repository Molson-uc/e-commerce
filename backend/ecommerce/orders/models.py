from collections.abc import Iterable
from datetime import timedelta
from django.db import models
from django.utils import timezone
from api.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    pay_day = models.DateTimeField(default=timezone.now() + timedelta(days=5))

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.order.first_name

    def get_cost(self):
        return self.product.price * self.quantity
