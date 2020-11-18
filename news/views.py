from django.shortcuts import render

from .models import News, Category

def index(request):
    news = News.objects.all()
    args = {
        'news':news,
    }
    return render(request,'news/index.html',args)
    
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    args = {
        'news':news,
        'category': category,
    }
    return render(request,'news/category.html',args)