from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductDetailView, ProductListView, ContactsView, PublicationDetailView, \
    PublicationCreateView, PublicationListView, PublicationUpdateView, PublicationDeleteView, ProductCreateView, \
    ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts_view'),
    path('products/<int:pk>', cache_page(300)(ProductDetailView.as_view()), name='product_detail'),
    path('products/new_product', ProductCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='update_product'),
    path('blog/', PublicationListView.as_view(), name='publication_list'),
    path('blog/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
    path('blog/new_post/', PublicationCreateView.as_view(), name='add_publication'),
    path('blog/<int:pk>/edit', PublicationUpdateView.as_view(), name='update_publication'),
    path('blog/<int:pk>/delete', PublicationDeleteView.as_view(), name='delete_publication'),
]
