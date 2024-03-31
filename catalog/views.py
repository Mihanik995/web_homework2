from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    template_name = 'main/home.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'main/products.html'
    model = Product


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): "{message}"')
        return redirect('contacts_view')
