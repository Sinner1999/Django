from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Тема')
    content = models.TextField(verbose_name = 'Текст')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name = 'Фото')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Дата последнего изменеения')
    is_published = models.BooleanField(default = True, verbose_name = 'Опубликован')
    category = models.ForeignKey(to = 'Category', on_delete = models.PROTECT, null = True, verbose_name = 'Категория')
    
    def get_absolute_url(self):
        return reverse(viewname = 'view_news', kwargs={'news_id': self.pk,})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at', '-title']
        
class Category(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Категория', db_index = True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(viewname = 'category', kwargs={'category_id': self.pk,})
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title',]