from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from webapp.models import Product, Category

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_view.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_add_view.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_add_view')

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_add_view.html'
    fields = ['name', 'description', 'category', 'price', 'image']
    success_url = reverse_lazy('products_view')