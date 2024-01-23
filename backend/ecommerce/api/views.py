from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, parsers
from .permissions import IsStaffPersmission
from .models import Product
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductCreateSerializer,
)


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
