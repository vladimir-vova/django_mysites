from django.shortcuts import render

from .models import News

def index(request):
    news = News.objects.all()
    args = {
        'news':news,
    }
    return render(request,'news/index.html',args)