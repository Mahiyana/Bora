from django.forms import ModelForm
from .models import ArticleCategory

class ArticleCategoryForm(ModelForm):
    class Meta:
        model = ArticleCategory
        fields = ['name']
