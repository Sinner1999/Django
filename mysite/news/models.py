from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title