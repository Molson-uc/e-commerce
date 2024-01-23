from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateDeleteView,
)

app_name = "api"

urlpatterns = [
    path("list/", ProductListView.as_view(), name="products-list"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("update/<int:pk>/", ProductUpdateDeleteView.as_view(), name="product-update"),
]
