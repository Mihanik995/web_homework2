from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_category_list_from_cache():
    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Category.objects.all()
            cache.set(key, cache_data)
    else:
        cache_data = Category.objects.all()

    return cache_data
