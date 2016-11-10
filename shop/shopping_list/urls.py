from django.conf.urls import url
from views import RegisterView, IndexView, CreateShoppingItems, CreateShopping

app_name = 'shopping_list'

urlpatterns = [
    url(r'^$', RegisterView.as_view(), name="register"),
    url(r'^shopping/$', IndexView.as_view(), name="index"),
    url(r'^shopping/(?P<pk>[0-9]+)/$', IndexView.as_view(), 
        name="shopping-items"),
    url(r'^shopping-items/$', CreateShoppingItems.as_view(),
        name="create-shop-items"),
    url(r'^create-shopping/$', CreateShopping.as_view(),
        name="create-shopping-list"),
]
