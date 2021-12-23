from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length = 150, label = "Назвавние")
    content = forms.CharField(label = "Текст")
    is_published = forms.BooleanField(label = "Опубликовано", initial = True)
    category = forms.ModelChoiceField(queryset = Category.objects.all(), label = "Категория", empty_label = 'Choose category...')
    