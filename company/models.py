from django.db import models


class Company(models.Model):
    established_year = models.IntegerField()
    experience_years = models.IntegerField()
    export_info = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    whatsapp_number = models.CharField(max_length=20)
    brochure = models.FileField(upload_to="brochures/", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="clients/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Industry(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IndustryItem(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="industries/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QualityTest(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class KnowledgeCard(models.Model):
    image = models.ImageField(upload_to="knowledge_cards/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    tagline = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pillar(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="pillars/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Certification(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="certifications/")
    file = models.FileField(upload_to="certifications/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class B2BInquiry(models.Model):
    company_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    product_interested = models.ForeignKey(
        "product.Product", on_delete=models.SET_NULL, null=True, blank=True
    )
    quantity_required = models.CharField(max_length=100)
    state_location = models.CharField(max_length=100)
    required_timeline = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.phone_number}"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ["order"]
