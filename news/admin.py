from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','content','created_ad','updated_ad','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('title','is_published')
    fields = ('title','category','content','photo','is_published','views',
        'created_ad','updated_ad')
    readonly_fields = ('views','created_ad','updated_ad')
    save_on_top = True
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)