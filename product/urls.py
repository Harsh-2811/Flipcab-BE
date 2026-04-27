from django.urls import path

from product.views import ProductCategoryListView, ProductDetailView, ProductListView

urlpatterns = [
    path(
        "categories/", ProductCategoryListView.as_view()
    ),  # GET /api/products/categories/
    path("", ProductListView.as_view()),  # GET /api/products/
    path("<slug:slug>/", ProductDetailView.as_view()),  # GET /api/products/house-wire/
]
