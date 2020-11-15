from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_ad','updated_ad','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')

admin.site.register(News, NewsAdmin)