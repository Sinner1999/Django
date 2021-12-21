from django import template
from news.models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_cat.html')
def show_categories():
    categories = Category.objects.all()
    
    content = {
        'category': categories,
    }
    
    return content