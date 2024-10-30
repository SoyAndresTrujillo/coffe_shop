from django.test import TestCase
from django.urls import reverse
from products.models import Product

# Create your tests here.


class ProductListViewTests(TestCase):
    def test_should_return_200(self):
        url = reverse("list_product")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_with_products(self):
        url = reverse("list_product")
        Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            available=True,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["products"]), 1)
