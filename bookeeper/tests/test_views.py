from django.test import TestCase, client
from django.core.urlresolvers import reverse
from book.models import Category, Book


class TestBookViews(TestCase):
    """ Test book views"""

    def setUp(self):
        self.client = Client()
        self.url_create_category = reserve('create_category')
        self.url_view_categories = reserve('view_category')
        self.url_create_book = reverse('create_book')
        self.url_view_book = reverse('view_book')
        self.url_search = reverse('search')
        self.book_name = {'name': " test_book"}
        self.category_name = {'name': " test_category"}
        self.create_category = Category.objects.create(name="History")
        self.create_books = Book.objects.create(
            name=self.book_name, category=self.create_category)

    def test_category_is_created(self):
        """Test that category is create from the frontend """
        initial_count = Category.objects.count()
        response = self.client.post(
            self.url_create_category, self.create_category)
        after_count = Category.objects.count()
        self.assertTrue(response.status_code, 201)
        self.assertEqual( after_count, initial_count+1 )
