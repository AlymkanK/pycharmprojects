from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from webapp.models import  Category, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list_view.html'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_edit_view.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list_view')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_edit_view.html'
    fields = ['name', 'description', 'category', 'price', 'image']
    success_url = reverse_lazy('products_view')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list_view')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('products_view')