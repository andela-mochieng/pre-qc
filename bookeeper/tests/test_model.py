from django.test import TestCase
from django.db.utils import IntegrityError
from book.models import Category, Book


class TestBookModels(TestCase):
    """Contains test for book models"""

    def setUp(self):
        self.book_name = "Test book name"
        self.all_books = Book.objects.all()
        self.create_category = Category.objects.create(name="History")
        self.create_books = Book.objects.create(
            name=self.book_name, category=self.create_category)

    def test_category_is_created(self):
        """Test that category model has one entry made in the setup"""
        category = Category.objects.all()
        category_name = category.values()[0]['name']
        self.assertEqual(len(category), 1)
        self.assertTrue(str(category_name), "History")

    def test_category_is_unique(self):
        """Test that book category names are unique"""
        with self.assertRaises(IntegrityError):
            same_category = Category.objects.create(name="History")

    def test_book_model_is_created(self):
        """Test that category model has one entry made in the setup"""
        book = Book.objects.count()
        self.assertEqual(book, 1)
        # self.assertTrue(str(book['name']), self.book_name)
