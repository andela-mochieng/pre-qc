from django.test import TestCase
from shopping_list.models import ShopItems, Shopping


class TestShoppingCatergory(TestCase):
    """Test shopping category represnted by the shopping Model"""

    def setUp(self):
        self.category1 = Shopping.objects.create(
            name="Christmas holiday shopping")
        self.shoppingitems = ShopItems.objects.create(items="Mountain bike")

    def test_shopping_category_is_created(self):
        before_entry = Shopping.objects.count()
        self.category1
        after_entry = Shopping.objects.count()
        self.assertEquals(after_entry, before_entry + 1)
