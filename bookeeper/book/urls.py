from django.conf.urls import url
from .views import Createcategory, ListCategory, add_book, ListBook
app_name = 'book'


urlpatterns = [
    url(r'^$', Createcategory.as_view(), name="create_category"),
    url(r'^category$', ListCategory.as_view(), name="view_category"),
    url(r'^book$', add_book, name="create_book"),
    url(r'^view_books$', ListBook.as_view(), name="view_book"),

]