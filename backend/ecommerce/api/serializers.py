from rest_framework import serializers
from .models import Product, Category


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerialzer()

    class Meta:
        model = Product
        fields = ["name", "category", "description", "price"]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerialzer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    category = CategorySerialzer()

    class Meta:
        model = Product
        fields = ["name", "image", "description", "price", "category"]

    def create(self, validated_data):
        category = validated_data.pop("category")
        foreign_key_instance = Category.objects.create(**category)
        instance = Product.objects.create(
            category=foreign_key_instance, **validated_data
        )
        return instance
