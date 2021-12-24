from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs = {"class": "form-control"}),
            'content': forms.Textarea(attrs = {"class": "form-control"}),
            'is_published': forms.CheckboxInput(attrs = {"class": "form-check-input", "role": "switch"}),
            'category': forms.Select(attrs = {"class": "form-control"}),
        }
    
    # title = forms.CharField(max_length = 150, label = "Назвавние", widget = forms.TextInput(attrs = {"class": "form-control"}))
    # content = forms.CharField(label = "Текст", widget = forms.Textarea(attrs = {"class": "form-control"}))
    # is_published = forms.BooleanField(label = "Опубликовано", initial = True, widget = forms.CheckboxInput(attrs = {"class": "form-check-input", "role": "switch"}))
    # category = forms.ModelChoiceField(queryset = Category.objects.all(), label = "Категория", empty_label = 'Choose category...', widget = forms.Select(attrs = {"class": "form-control"}))
    