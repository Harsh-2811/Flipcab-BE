from rest_framework import generics

from company.models import (
    FAQ,
    B2BInquiry,
    Certification,
    Client,
    Company,
    Industry,
    KnowledgeCard,
    Pillar,
    QualityTest,
    Testimonial,
)
from company.serializers import (
    B2BInquirySerializer,
    CertificationSerializer,
    ClientSerializer,
    CompanySerializer,
    FAQSerializer,
    IndustrySerializer,
    KnowledgeCardSerializer,
    PillarSerializer,
    QualityTestSerializer,
    TestimonialSerializer,
)


class CompanyDetailView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer

    def get_object(self):
        return Company.objects.first()


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class IndustryListView(generics.ListAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class QualityTestListView(generics.ListAPIView):
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer


class KnowledgeCardListView(generics.ListAPIView):
    queryset = KnowledgeCard.objects.all()
    serializer_class = KnowledgeCardSerializer


class PillarListView(generics.ListAPIView):
    queryset = Pillar.objects.all()
    serializer_class = PillarSerializer


class CertificationListView(generics.ListAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class B2BInquiryCreateView(generics.CreateAPIView):
    queryset = B2BInquiry.objects.all()
    serializer_class = B2BInquirySerializer


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


def download_brochure(request):
    import os

    from django.conf import settings
    from django.http import FileResponse, Http404

    file_path = os.path.join(
        settings.BASE_DIR,
        "company",
        "brochures",
        "Flipcab_company_profile_Modified.pdf",
    )
    if os.path.exists(file_path):
        response = FileResponse(
            open(file_path, "rb"),
            content_type="application/pdf",
            as_attachment=True,
            filename="Flipcab_company_profile_Modified.pdf",
        )
        return response
    raise Http404("Brochure not found")
