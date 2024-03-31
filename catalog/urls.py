from django.urls import path

from catalog.views import ProductDetailView, ProductListView, ContactsView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts_view'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]