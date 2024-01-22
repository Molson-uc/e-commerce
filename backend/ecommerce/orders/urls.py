from django.urls import path, include
from .views import OrderList, OrderCreate, OrderUpdate

app_name = "orders"

urlpatterns = [
    path("list/", OrderList.as_view(), name="order-list"),
    path("create/", OrderCreate.as_view(), name="order-create"),
    path("update/", OrderUpdate.as_view(), name="order-update"),
]
