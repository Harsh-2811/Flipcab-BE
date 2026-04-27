from rest_framework import serializers

from company.models import (
    FAQ,
    B2BInquiry,
    Certification,
    Client,
    Company,
    Industry,
    IndustryItem,
    KnowledgeCard,
    Pillar,
    QualityTest,
    Testimonial,
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "logo"]


class IndustryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryItem
        fields = ["id", "title", "image"]


class IndustrySerializer(serializers.ModelSerializer):
    items = IndustryItemSerializer(many=True, source="industryitem_set", read_only=True)

    class Meta:
        model = Industry
        fields = ["id", "name", "items"]


class QualityTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityTest
        fields = ["id", "name", "description"]


class KnowledgeCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeCard
        fields = ["id", "image", "title", "description", "tagline"]


class PillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pillar
        fields = ["id", "title", "icon"]


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ["id", "name", "image", "file"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "name", "review", "rating"]


class B2BInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = B2BInquiry
        fields = [
            "id",
            "company_name",
            "phone_number",
            "email",
            "product_interested",
            "quantity_required",
            "state_location",
            "required_timeline",
            "message",
        ]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "order"]
