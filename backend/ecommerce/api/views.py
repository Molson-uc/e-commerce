from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Coalesce
from django.db.models import Sum
from rest_framework import generics, filters, parsers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Sum
from orders.models import OrderItem

from .permissions import IsStaffPersmission
from .models import Product
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductCreateSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["name", "category__name", "price"]
    filterset_fields = ["name", "category", "description", "price"]


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    permission_classes = [IsStaffPersmission]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"
    permission_classes = [IsStaffPersmission]


class TopProductsView(APIView):
    def get(self, request):
        # Pobierz dane wejściowe z parametrów zapytania
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        num_products = request.query_params.get("num_products", 5)
        num_products = int(num_products)
        try:
            start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return Response(
                {"error": "Niepoprawny format daty. Użyj formatu YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        top_products = (
            OrderItem.objects.filter(order__created__date__range=[start_date, end_date])
            .values("product__name", "product__id")
            .annotate(total_quantity=Sum("quantity"))
            .order_by("-total_quantity")[:num_products]
        )

        # Przygotuj dane wyjściowe
        result = []
        for product in top_products:
            result.append(
                {
                    "product_id": product["product__id"],
                    "product_name": product["product__name"],
                    "total_quantity": product["total_quantity"],
                }
            )

        return Response(result, status=status.HTTP_200_OK)
