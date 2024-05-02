from catalog.models import Category


def get_category_list():
    return Category.objects.all()