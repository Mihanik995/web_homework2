from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {'object_list': Product.objects.all()}
    return render(request, 'main/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): "{message}"')
    return render(request, 'main/contacts.html')

def products(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'main/products.html', context)
