from django.test import TestCase
from . models import Photo, Category
# Create your tests here.
class PhotoTest(TestCase):
    def setUp(self):
        self.photo = Photo(description='Test Photo', image='test_image.jpg', category=Category(name='Test Category'))
    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Photo))

    def test_save_photo(self):
        self.photo.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='Test Category')
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)