from django.forms import ModelForm
from .models import ArticleCategory, Article, Gallery, Artwork, User, Event, Report, Review, ReviewItem, ReviewCategory, News, NewsCategory

class ArticleCategoryForm(ModelForm):
    class Meta:
        model = ArticleCategory
        fields = ['name']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description']

class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ['gallery', 'title', 'description', 'image']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'art_name', 'op_name', 'aliik', 'story', 'about', 'rank']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'introduction', 'ending', 'year', 'description']

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['image', 'report']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating', 'item']

class ReviewItemForm(ModelForm):
    class Meta:
        model = ReviewItem
        fields = ['category', 'title', 'cover', 'org_title', 'author', 'translator']

class NewsCategoryForm(ModelForm):
    class Meta:
        model = NewsCategory
        fields = ['name']

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category']
