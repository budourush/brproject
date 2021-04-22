from .models import Category, Tag


def blog_commons(request):
    context = {
        'category_list': Category.objects.all(),
        'tag_list': Tag.objects.all()
    }
    return context
