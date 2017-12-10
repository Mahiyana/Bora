from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleCategoryForm, ArticleForm

def index(request):
    return render(request, 'base.html')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', {'article': article})

def add_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/artykuly')
    else:
        form =  ArticleForm()
    return render(request, 'add_article.html', {'form': form})

def add_article_category(request):
    form = ArticleCategoryForm()
    if request.method == 'POST':
        form = ArticleCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/artykuly')
    else:
        form =  ArticleCategoryForm()
    return render(request, 'add_article_category.html', {'form': form})
