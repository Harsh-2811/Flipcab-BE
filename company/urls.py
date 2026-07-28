from django.urls import path

from company.views import (
    B2BInquiryCreateView,
    CertificationListView,
    ClientListView,
    CompanyDetailView,
    FAQListView,
    IndustryListView,
    KnowledgeCardListView,
    PillarListView,
    QualityTestListView,
    TestimonialListView,
    download_brochure,
)

urlpatterns = [
    path("", CompanyDetailView.as_view()),  # GET  /api/company/
    path("clients/", ClientListView.as_view()),  # GET  /api/company/clients/
    path("industries/", IndustryListView.as_view()),  # GET  /api/company/industries/
    path(
        "quality-tests/", QualityTestListView.as_view()
    ),  # GET  /api/company/quality-tests/
    path(
        "knowledge-cards/", KnowledgeCardListView.as_view()
    ),  # GET  /api/company/knowledge-cards/
    path("pillars/", PillarListView.as_view()),  # GET  /api/company/pillars/
    path(
        "certifications/", CertificationListView.as_view()
    ),  # GET  /api/company/certifications/
    path(
        "testimonials/", TestimonialListView.as_view()
    ),  # GET  /api/company/testimonials/
    path("inquiry/", B2BInquiryCreateView.as_view()),  # POST /api/company/inquiry/
    path(
        "download-brochure/", download_brochure
    ),  # GET /api/company/download-brochure/
    path("faqs/", FAQListView.as_view()),  # GET  /api/company/faqs/
]
