from django.test import TestCase
from django.urls import reverse

from .models import Category, Subcategory, Product


class SimpleDataMixin:
    def create_sample_catalog(self):
        self.cat = Category.objects.create(name="Test Cat", slug="test-cat")
        self.sub = Subcategory.objects.create(
            name="Subcat", slug="subcat", category=self.cat
        )
        self.prod = Product.objects.create(
            name="Prod", slug="prod", subcategory=self.sub
        )


class ModelTests(SimpleDataMixin, TestCase):
    def setUp(self):
        self.create_sample_catalog()

    def test_category_counts(self):
        self.assertEqual(self.cat.subcategory_count, 1)
        self.assertEqual(self.cat.product_count, 1)
        self.assertEqual(self.sub.product_count, 1)

    def test_product_category_property(self):
        self.assertEqual(self.prod.category, self.cat)


class ViewTests(SimpleDataMixin, TestCase):
    def setUp(self):
        self.create_sample_catalog()

    def test_category_list_view(self):
        resp = self.client.get(reverse("products:category_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.cat.name)

    def test_category_detail_view(self):
        resp = self.client.get(
            reverse("products:category_details", kwargs={"slug": self.cat.slug})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.cat.name)

    def test_subcategory_detail_view(self):
        resp = self.client.get(
            reverse("products:subcategory_details", kwargs={"slug": self.sub.slug})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.sub.name)

    def test_product_detail_view(self):
        resp = self.client.get(
            reverse("products:product_details", kwargs={"slug": self.prod.slug})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.prod.name)

    def test_product_list_view(self):
        resp = self.client.get(reverse("products:product_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.prod.name)

    def test_product_missing_view(self):
        # accessing bare "product/" should render a friendly message rather
        # than a 404.
        resp = self.client.get(reverse("products:product_missing"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "No Product Selected")

