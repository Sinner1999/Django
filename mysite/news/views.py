from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.
def index(request):
    news = News.objects.all()
    content = {
        'news' : news,
        'title': 'News list'
    }
    
    return render(request, 'news/index.html', content)


