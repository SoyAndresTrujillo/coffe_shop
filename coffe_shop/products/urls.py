from django.urls import path
from .views import ProductListView, ProductList

urlpatterns = [
    path("add/", ProductListView.as_view(), name="add_product"),
    path("list/", ProductList.as_view(), name="list_product"),
]
