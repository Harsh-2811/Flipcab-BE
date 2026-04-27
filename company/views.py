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
