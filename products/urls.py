from django.urls import path
from .views import ProductAddView, ProductListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("add/", ProductAddView.as_view(), name="add_product"),
    path("", ProductListView.as_view(), name="list_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
