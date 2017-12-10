from django.forms import ModelForm
from .models import ArticleCategory, Article

class ArticleCategoryForm(ModelForm):
    class Meta:
        model = ArticleCategory
        fields = ['name']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'author']
