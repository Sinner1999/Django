from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm


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
        'title': 'News list by category',
        'id': category_id,
    }

    return render(request, 'news/index.html', content)

def view_news(request, news_id):
    
    # news_item = News.objects.get(pk = news_id)
    news_item = get_object_or_404(News, pk = news_id)
    
    
    
    content = {
        'news_item': news_item,
        
    }
    
    return render(request, 'news/view_news.html', content)

def add_news(request):
    
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
        
    content = {
        'form': form,
    }
    
    return render(request, 'news/add_news.html', content)
