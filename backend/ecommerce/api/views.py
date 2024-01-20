from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from rest_framework import generics, filters

from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["name", "category__name", "price"]
    filterset_fields = ["name", "category", "description", "price"]
