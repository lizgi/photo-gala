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


class photosTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        photos.objects.create(
            name="Test photos",
            image_description="Test Description",
            location=Location.objects.create(value="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="http://test.com/test.jpg",
            post_date="Test image"
        )

    def test_image_name(self):
        """
        Test that the image name is correct
        """
        image = photos.objects.get(name="Test photos")
        self.assertEqual(image.name, "Test photos")

    def test_image_description(self):
        """
        Test that the image description is correct
        """
        image = photos.objects.get(name="Test photos")
        self.assertEqual(image.image_description, "Test Description")

    def test_image_location(self):
        """
        Test that the image location is correct
        """
        image = photos.objects.get(name="Test photos")
        self.assertEqual(image.location.value, "Test Location")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = photos.objects.get(name="Test photos")
        self.assertEqual(image.category.name, "Test Category")

    

    def test_image_str(self):
        """
        Test that the image string representation is correct
        """
        image = photos.objects.get(name="Test photos")
        self    