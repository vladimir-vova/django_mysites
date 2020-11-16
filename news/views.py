from django.shortcuts import render

from .models import News, Category

def index(request):
    news = News.objects.all()
    category = Category.objects.all()
    args = {
        'news':news,
        'category': category,
    }
    return render(request,'news/index.html',args)
    
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    args = {
        'news':news,
        'categories': categories,
        'category': category,
    }
    return render(request,'news/category.html',args)