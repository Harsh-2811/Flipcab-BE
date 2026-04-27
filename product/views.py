from rest_framework import generics
from rest_framework.response import Response

from product.models import Category, Product
from product.serializers import (
    ProductCategorySerializer,
    ProductDetailSerializer,
    ProductListSerializer,
)


class ProductCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        related = Product.objects.filter(category=instance.category).exclude(
            id=instance.id
        )[:4]
        data["related_products"] = ProductListSerializer(
            related, many=True, context={"request": request}
        ).data

        return Response(data)
