from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, UpdateView, CreateView

from catalog.models import Product, Publication


class ProductListView(ListView):
    template_name = 'main/home.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'main/products.html'
    model = Product


class PublicationCreateView(CreateView):
    template_name = 'main/blog_form.html'
    model = Publication
    fields = ('title', 'text',)
    success_url = reverse_lazy('publication_list')


class PublicationListView(ListView):
    template_name = 'main/blog_view.html'
    model = Publication


class PublicationDetailView(DetailView):
    template_name = 'main/blog_detail.html'
    model = Publication


class PublicationUpdateView(UpdateView):
    template_name = 'main/blog_form.html'
    model = Publication
    fields = ('title', 'text', 'preview',)
    success_url = reverse_lazy('publication_list')


class PublicationDeleteView(DeleteView):
    template_name = 'main/blog_delete.html'
    model = Publication
    success_url = reverse_lazy('publication_list')


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): "{message}"')
        return redirect('contacts_view')
