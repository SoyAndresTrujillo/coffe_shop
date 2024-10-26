from django.views import generic
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product

# Create your views here.


class ProductListView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductList(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
