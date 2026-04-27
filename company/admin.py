from django.contrib import admin

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


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "phone",
        "email",
        "experience_years",
        "created_at",
        "updated_at",
    ]
    search_fields = ["phone", "email", "address", "export_info"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(IndustryItem)
class IndustryItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "industry", "created_at", "updated_at"]
    search_fields = ["title", "industry__name"]
    list_filter = ["industry", "created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(QualityTest)
class QualityTestAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    search_fields = ["name", "description"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(KnowledgeCard)
class KnowledgeCardAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "tagline", "created_at", "updated_at"]
    search_fields = ["title", "tagline", "description"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(Pillar)
class PillarAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    search_fields = ["title"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rating", "created_at", "updated_at"]
    search_fields = ["name", "review"]
    list_filter = ["rating", "created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(B2BInquiry)
class B2BInquiryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "company_name",
        "phone_number",
        "email",
        "product_interested",
        "submitted_at",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "company_name",
        "phone_number",
        "email",
        "state_location",
        "product_interested__name",
    ]
    list_filter = ["product_interested", "submitted_at", "created_at", "updated_at"]
    ordering = ("-created_at",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "order", "created_at", "updated_at"]
    search_fields = ["question", "answer"]
    list_filter = ["created_at", "updated_at"]
    ordering = ("order", "-created_at")
