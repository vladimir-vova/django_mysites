from django.db import models


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    title = models.CharField(max_length=150,verbose_name='Наименование')
    content = models.TextField(blank=True,verbose_name='Содержание')
    created_ad = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated_ad = models.DateTimeField(auto_now=True,verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фото',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='Опубликован')
    category = models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name='Категория')
    
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    title = models.CharField(max_length=150,db_index=True,verbose_name='Наименование категории')
        
    def __str__(self):
        return self.title