from django.urls import path
from .views import *

app_name = "news"

urlpatterns = [
    path('', index, name="index"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('news/<int:news_id>/', view_news, name="view_news"),
    path('news/add-news/', add_news, name="add_news"),
]