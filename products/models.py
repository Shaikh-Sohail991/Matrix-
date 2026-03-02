import json

from django.db import models


class Category(models.Model):
    """High‑level product grouping, e.g. "Industrial Equipment".

    Subcategories and products are linked through related objects.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/images/", null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    @property
    def subcategory_count(self):
        # using related_name below
        return self.subcategories.count()

    @property
    def product_count(self):
        # count all products underneath this category
        return Product.objects.filter(subcategory__category=self).count()


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="subcategories/images/", null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.products.count()


class Product(models.Model):
    subcategory = models.ForeignKey(
        Subcategory,
        related_name="products",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    # marketing flags
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    image = models.ImageField(upload_to="products/images/", null=True, blank=True)
    documentation = models.FileField(upload_to="products/docs/", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def category(self):
        # convenience property used by templates
        return self.subcategory.category if self.subcategory else None

    @property
    def quick_specs(self):
        # Return the first few specifications as quick specs
        return self.specs.all()[:3]

    @property
    def specs_json(self):
        """Return specs as a JSON string for use in data-specs attribute."""
        return json.dumps([{"label": s.label, "value": s.value} for s in self.specs.all()])

    @property
    def specifications(self):
        # complex table structure
        return self.specs.all()

    @property
    def features(self):
        # list of features related to this product
        return self.product_features.all()


class ProductImage(models.Model):
    """Optional gallery images for a product."""
    product = models.ForeignKey(
        Product,
        related_name="gallery",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.name} image"

    @property
    def url(self):
        return self.image.url


class Spec(models.Model):
    """Dynamic specification for a product. Can add unlimited specs."""
    product = models.ForeignKey(
        Product,
        related_name="specs",
        on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=255, help_text="e.g., 'Power Output', 'Speed', 'Voltage'")
    value = models.CharField(max_length=255, help_text="e.g., '500W', '3000 RPM', '220V'")

    class Meta:
        verbose_name_plural = "Specs"

    def __str__(self):
        return f"{self.product.name} - {self.label}: {self.value}"


class Feature(models.Model):
    """Dynamic feature for a product. Can add unlimited features."""
    product = models.ForeignKey(
        Product,
        related_name="product_features",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, help_text="e.g., 'Advanced Technology'")
    description = models.TextField(help_text="Detailed description of the feature")

    def __str__(self):
        return f"{self.product.name} - {self.title}"


class Quote(models.Model):
    """Quote requests submitted from product details page."""
    product_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Quote Request from {self.full_name} for {self.product_name}"


class CatalogRequest(models.Model):
    """Documentation / catalog access requests submitted from product details page."""
    product_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Catalog Request"
        verbose_name_plural = "Catalog Requests"

    def __str__(self):
        return f"Catalog Request from {self.full_name} for {self.product_name}"
