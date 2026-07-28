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

    from django.http import FileResponse, Http404

    from company.models import Company

    company = Company.objects.first()
    if company and company.brochure:
        try:
            response = FileResponse(
                company.brochure.open("rb"),
                content_type="application/pdf",
                as_attachment=True,
                filename=os.path.basename(company.brochure.name),
            )
            return response
        except FileNotFoundError:
            raise Http404("Brochure file not found on disk")
    raise Http404("No brochure configured in admin")
