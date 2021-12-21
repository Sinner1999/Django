from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.
def index(request):
    news = News.objects.all()
    # category = Category.objects.all()
    content = {
        'news' : news,
        'title': 'News list',
    }
    
    return render(request, 'news/index.html', content)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    # category = Category.objects.all()
    content = {
        'news' : news,
        'title': 'News list',
        'id': category_id,
    }

    return render(request, 'news/index.html', content)
