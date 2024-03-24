from django.urls import path

from catalog.views import home, contacts, products

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/<int:pk>', products)
]