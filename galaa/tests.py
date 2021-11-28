from django.test import TestCase
from .models import Location, Category, photos

# Create your tests here.

# location model tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(value="Test Location")

    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(value="Test Location")
        self.assertEqual(location.value, "Test Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(value="Test Location")
        self.assertEqual(str(location), "Test Location")

class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")




