from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin

def test(request):
    objects = ['join1','join2','join3','join4',
    'join5','join6','join7','join8','join9',
    'join5','join6','join7','join8','join9',
    'join5','join6','join7','join8','join9',
    'join5','join6','join7','join8','join9',
    'join5','join6','join7','join8','join9']

    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test.html',{'page_obj':page_obj})


class HomeNews(MyMixin, ListView):
    model = News #аналог news = News.objects.all()
    template_name = 'news/index.html'
    context_object_name = 'news'
    mixin_prop = 'Hello, world!!!'
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


#def index(request):
#    news = News.objects.all()
#    args = {
#        'news':news,
#    }
#    return render(request,'news/index.html',args)

class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')
    
#def get_category(request, category_id):
#    news = News.objects.filter(category_id=category_id)
    # category = Category.objects.get(pk=category_id)
#    category = get_object_or_404(Category, pk=category_id)
#    args = {
#        'news':news,
#        'category': category,
#    }
#    return render(request,'news/category.html',args)

class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'
    
    
#def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
#    news_item = get_object_or_404(News, pk=news_id)
#    args = {
#        'news_item': news_item,
#    }
#    return render(request,'news/view_news.html', args)

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('news:index')
    login_url = reverse_lazy('news:index')
    
    
    
#def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('news:index')
#    else:
#        form = NewsForm()
#    args = {
#        'form' : form,
#    }
#    return render(request, 'news/add_news.html', args)