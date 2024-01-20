from rest_framework import serializers
from .models import Product, Category


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerialzer()

    class Meta:
        model = Product
        fields = ["name", "category", "description", "price"]
