from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm

from django.views.generic import ListView, DetailView, CreateView
    

class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Main Page'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published = True).select_related('category')
    
class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2
    
    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published = True).select_related('category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'News by category'
        return context
    
class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template_name = 'news/view_news_detail.html'
    context_object_name = 'news_item'
    
    
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/login/?next=/news/add_news'
    


# Create your views here.
# def index(request):
#     news = News.objects.all()
#     # category = Category.objects.all()
#     content = {
#         'news' : news,
#         'title': 'News list',
#     }
    
    # return render(request, 'news/index.html', content)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id = category_id)
#     # category = Category.objects.all()
#     content = {
#         'news' : news,
#         'title': 'News list by category',
#         'id': category_id,
#     }

    # return render(request, 'news/index.html', content)

# def view_news(request, news_id):
    
#     # news_item = News.objects.get(pk = news_id)
#     news_item = get_object_or_404(News, pk = news_id)
    
    
    
#     content = {
#         'news_item': news_item,
        
#     }
    
#     return render(request, 'news/view_news.html', content)

# def add_news(request):
    
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
        
#     content = {
#         'form': form,
#     }
    
#     return render(request, 'news/add_news.html', content)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, 'User added')
            return redirect('home')
        else:
            messages.error(request, 'Non valid data')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'news/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Non valid data')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'news/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')