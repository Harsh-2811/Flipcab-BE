from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    about = models.TextField()
    thumbnail = models.ImageField(upload_to="products/thumbnails/")
    datasheet = models.FileField(
        upload_to="products/datasheets/", null=True, blank=True
    )
    voltage_range = models.CharField(max_length=100)
    size_range = models.CharField(max_length=100)
    temperature_rating = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return f"Image for {self.product.name}"


class KeyFeature(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="key_features"
    )
    features = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.features} - {self.product.name}"


class SpecRow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")
    conductor_area = models.CharField(max_length=100)
    no_of_wires = models.CharField(max_length=100)
    ins_thickness = models.CharField(max_length=100)
    overall_dia = models.CharField(max_length=100)
    resistance = models.CharField(max_length=100)
    current_rating = models.CharField(max_length=100)

    def __str__(self):
        return f"Spec for {self.product.name}"


class Certification(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="certifications"
    )
    name = models.CharField(max_length=100)
    badge_image = models.ImageField(upload_to="products/certifications/")

    def __str__(self):
        return self.name
