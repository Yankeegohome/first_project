from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название", widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Текст новости", required=False, widget=forms.Textarea(attrs={"class": "form-control",
                                                                                                  "rows": 3
                                                                                                  }))
    is_published = forms.BooleanField(label="Опубликовано?", initial=True, widget=forms.NullBooleanSelect(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(empty_label="Выберите категорию",label="Категория", queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))


