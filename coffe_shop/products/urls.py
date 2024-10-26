from django.urls import path
from .views import ProductListView

urlpatterns = [
    path("add/", ProductListView.as_view(), name="add_product"),
]
