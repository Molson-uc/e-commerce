from django.shortcuts import render
from rest_framework import generics
from .models import Product


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
