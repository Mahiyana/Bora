from django.forms import ModelForm
from .models import ArticleCategory, Article, Gallery, Artwork

class ArticleCategoryForm(ModelForm):
    class Meta:
        model = ArticleCategory
        fields = ['name']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'author']

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description']

class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ['author', 'gallery', 'title', 'description', 'image']
