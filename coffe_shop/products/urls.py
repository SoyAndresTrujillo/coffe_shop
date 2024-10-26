from django.urls import path
from .views import ProductAddView, ProductListView

urlpatterns = [
    path("add/", ProductAddView.as_view(), name="add_product"),
    path("", ProductListView.as_view(), name="list_product"),
]
