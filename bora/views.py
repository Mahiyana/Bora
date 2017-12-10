from django.shortcuts import render
from .models import Article
from .forms import ArticleCategoryForm

def index(request):
    return render(request, 'base.html')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', {'article': article})

def add_article_category(request):
    form = ArticleCategoryForm()
    return render(request, 'add_article_category.html', {'form': form})
