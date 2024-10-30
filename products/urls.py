from django.urls import path
from .views import ProductAddView, ProductListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("add/", ProductAddView.as_view(), name="add_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
