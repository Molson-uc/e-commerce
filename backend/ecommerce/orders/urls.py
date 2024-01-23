from django.urls import path, include
from .views import OrderListView, OrderCreateView, OrderUpdateView

app_name = "orders"

urlpatterns = [
    path("list/", OrderListView.as_view(), name="order-list"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("update/", OrderUpdateView.as_view(), name="order-update"),
]
