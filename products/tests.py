from decimal import Decimal
from django.test import TestCase
from .models import Category, Subcategory, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(category_name="Electronics")

    def test_category_creation(self):
        category = Category.objects.get(category_name="Electronics")
        self.assertEqual(category.category_name, "Electronics")

class ProductModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(category_name="Electronics")
        sub_category = Subcategory.objects.create(category=category, sub_category_name="Laptops")
        Product.objects.create(product_name="MacBook Pro", price=Decimal("1299.99"), is_active=True, category=category, sub_category=sub_category)

    def test_product_creation(self):
        product = Product.objects.get(product_name="MacBook Pro")
        self.assertEqual(product.price, Decimal("1299.99")) 
        self.assertTrue(product.is_active)


# This is for testing purpose...