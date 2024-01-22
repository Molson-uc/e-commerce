from rest_framework import serializers
from .models import Order, OrderItem
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name")


class OrderItemSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "quantity",
            "price",
            "cost",
        )

    def get_price(self, obj):
        return obj.product.price

    def get_cost(self, obj):
        return obj.get_cost()


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "items",
            "postal_code",
            "city",
        )

    def create(self, validated_data):
        orders_data = validated_data.pop("items")
        print(f"heloo: {orders_data}")
        order = Order.objects.create(**validated_data)
        print(f"order:  {order}")

        for order_data in orders_data:
            OrderItem.objects.create(order=order, **order_data)

        return order

    def update(self, instance, validated_data):
        orders_data = validated_data.pop("items", None)
        orders = list((instance.order_items).all())

        if orders_data:
            for order_data in orders_data:
                order = orders.pop(0)
                order.product = order_data.get("product", order.product)
                order.quantity = order_data.get("quantity", order.quantity)
                order.save()

        return instance


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "email",
            "address",
            "postal_code",
            "city",
            "items",
        )
