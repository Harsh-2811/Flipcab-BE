from rest_framework import serializers

from product.models import Category, Certification, Image, KeyFeature, Product, SpecRow


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image"]


class ProductKeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ["id", "features", "order"]


class ProductSpecRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecRow
        fields = [
            "id",
            "conductor_area",
            "no_of_wires",
            "ins_thickness",
            "overall_dia",
            "resistance",
            "current_rating",
        ]


class ProductCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ["id", "name", "badge_image"]


# Product List — simple, used on product listing page
class ProductListSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "short_description", "thumbnail", "category"]


# Product Detail — full data, used on product detail page
class ProductDetailSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    images = ProductImageSerializer(many=True)
    key_features = ProductKeyFeatureSerializer(many=True)
    specs = ProductSpecRowSerializer(many=True)
    certifications = ProductCertificationSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "about",
            "thumbnail",
            "datasheet",
            "voltage_range",
            "size_range",
            "temperature_rating",
            "category",
            "images",
            "key_features",
            "specs",
            "certifications",
        ]
