from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, UpdateView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product, Publication


class ProductListView(ListView):
    template_name = 'main/home.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'main/products.html'
    model = Product

class ProductCreateView(CreateView):
    template_name = 'main/product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products_list')

class ProductUpdateView(UpdateView):
    template_name = 'main/product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products_list')


class PublicationCreateView(CreateView):
    template_name = 'main/blog_form.html'
    model = Publication
    fields = ('title', 'text',)
    success_url = reverse_lazy('publication_list')

    def form_valid(self, form):
        if form.is_valid():
            new_publication = form.save()
            new_publication.slug = slugify(new_publication.title)
            new_publication.save()

        return super().form_valid(form)


class PublicationListView(ListView):
    template_name = 'main/blog_view.html'
    model = Publication

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PublicationDetailView(DetailView):
    template_name = 'main/blog_detail.html'
    model = Publication

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class PublicationUpdateView(UpdateView):
    template_name = 'main/blog_form.html'
    model = Publication
    fields = ('title', 'text', 'preview',)

    def get_success_url(self):
        return reverse('publication_detail', args=[self.kwargs.get('pk')])


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
