from django.contrib import admin
from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate

urlpatterns = [
    path("list/", ProductList.as_view(), name="products-list"),
    path("detail/<str:slug>/", ProductDetail.as_view(), name="product-detail"),
    path("create/", ProductCreate.as_view(), name="product-create"),
]
