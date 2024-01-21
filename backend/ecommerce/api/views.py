from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, filters

from .models import Product
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductCreateSerializer,
)


class ProductList(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["name", "category__name", "price"]
    filterset_fields = ["name", "category", "description", "price"]


class ProductDetail(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = "slug"


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
