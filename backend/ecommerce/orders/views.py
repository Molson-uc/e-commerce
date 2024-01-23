from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderItem, OrderListSerializer
from .permissions import IsClientPermission
from .tasks import order_created


class OrderItemCreateView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItem
    lookup_field = "pk"
    parser_classes = (JSONParser,)


class OrderCreateView(generics.CreateAPIView):
    permission_classes = [IsClientPermission]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    parser_classes = (JSONParser,)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        id = data["id"]
        order = Order.objects.get(id=id)
        modified_data = {
            "get_total_cost": order.get_total_cost(),
            "pay_day": order.pay_day,
        }
        order_created.delay(order.id)

        return Response(modified_data, status=response.status_code)


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderUpdateView(generics.UpdateAPIView):
    permission_classes = [IsClientPermission]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    lookup_field = "pk"
