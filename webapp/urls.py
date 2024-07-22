
from django.urls import path

from views.category import *
from views.views import products_view, ProductDetailView, CategoryCreateView, ProductCreateView

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add_view'),
path('categories/', CategoryListView.as_view(), name='category_list_view'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit_view'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete_view'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
]
