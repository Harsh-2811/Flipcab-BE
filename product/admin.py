from django.contrib import admin

from product.models import Category, Certification, Image, KeyFeature, Product, SpecRow


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    search_fields = ["name", "slug"]
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
        "slug",
        "voltage_range",
        "size_range",
        "temperature_rating",
    ]
    search_fields = ["name", "slug", "category__name", "short_description", "about"]
    list_filter = ["category"]
    ordering = ("name",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "product"]
    search_fields = ["product__name"]
    list_filter = ["product"]
    ordering = ("-id",)


@admin.register(KeyFeature)
class KeyFeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "features", "order"]
    search_fields = ["product__name"]
    list_filter = ["product"]
    ordering = ("product", "order")


@admin.register(SpecRow)
class SpecRowAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "conductor_area",
        "no_of_wires",
        "ins_thickness",
        "overall_dia",
        "resistance",
        "current_rating",
    ]
    search_fields = ["product__name", "conductor_area", "ins_thickness", "overall_dia"]
    list_filter = ["product"]
    ordering = ("product", "-id")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "product"]
    search_fields = ["name", "product__name"]
    list_filter = ["product"]
    ordering = ("name",)
