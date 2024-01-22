from rest_framework import generics
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderItem, OrderListSerializer
from .permissions import IsClientPermission


class OrderItemCreate(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItem
    lookup_field = "slug"


class OrderCreate(generics.CreateAPIView):
    # permission_classes = [IsClientPermission]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        id = data["id"]
        order = Order.objects.get(id=id)
        modified_data = {
            "get_total_cost": order.get_total_cost(),
            "created": order.created,
            "pay_day": order.pay_day,
        }

        return Response(modified_data, status=response.status_code)


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderUpdate(generics.UpdateAPIView):
    permission_classes = [IsClientPermission]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    lookup_field = "slug"
