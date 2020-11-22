from django.shortcuts import render, get_object_or_404

from .models import News, Category

def index(request):
    news = News.objects.all()
    args = {
        'news':news,
    }
    return render(request,'news/index.html',args)
    
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)
    args = {
        'news':news,
        'category': category,
    }
    return render(request,'news/category.html',args)
    
def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    args = {
        'news_item': news_item,
    }
    return render(request,'news/view_news.html', args)