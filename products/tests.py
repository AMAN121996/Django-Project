from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def test_product_creation(self):
        p = Product.objects.create(name="Laptop", description="Fast", price=1200.99)
        self.assertEqual(p.name, "Laptop")
