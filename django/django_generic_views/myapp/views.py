from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from myapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 3


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')
    template_name = 'product_delete.html'
