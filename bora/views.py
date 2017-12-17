from django.shortcuts import render, redirect
from .models import Article, Gallery, Artwork, User
from .forms import ArticleCategoryForm, ArticleForm, GalleryForm, ArtworkForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'base.html')

def articles(request):
    articles = Article.objects.all()
    grouped_articles = {}
    other = []
    for article in articles:
        if article.category is None:
          other.append(article)
          continue
        if article.category.name not in grouped_articles:
          grouped_articles[article.category.name] = []
        grouped_articles[article.category.name].append(article)
    if len(other) > 0:
        grouped_articles['Inne'] = other
    return render(request, 'articles.html', {'grouped_articles': grouped_articles, 'other' : other})

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', {'article': article})

@login_required
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

@login_required
def edit_article(request, id):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=Article.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(form.instance)
    else:
        form =  ArticleForm(instance=Article.objects.get(id=id))
    return render(request, 'edit_article.html', {'form': form})


@login_required
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

def galleries(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries.html', {'galleries': galleries})

def gallery(request, id):
    gallery = Gallery.objects.get(id=id)
    return render(request, 'gallery.html', {'gallery': gallery})

@login_required
def add_gallery(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/galerie')
    else:
        form =  GalleryForm()
    return render(request, 'add_gallery.html', {'form': form})

@login_required
def edit_gallery(request, id):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=Gallery.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('/galerie')
    else:
        form =  GalleryForm(instance=Gallery.objects.get(id=id))
    return render(request, 'edit_gallery.html', {'form': form})

@login_required
def add_artwork(request):
    form = ArtworkForm()
    if request.method == 'POST':
        print(request.POST)
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/galerie')
    else:
        form =  ArtworkForm()
    return render(request, 'add_artwork.html', {'form': form})

def artwork(request, id):
    artwork = Artwork.objects.get(id=id)
    return render(request, 'artwork.html', {'artwork':artwork})

@login_required
def edit_artwork(request, id):
    form = ArtworkForm()
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=Artwork.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(form.instance)
    else:
        form =  ArtworkForm(instance=Artwork.objects.get(id=id))
    return render(request, 'edit_artwork.html', {'form': form})

def members(request):
    return render(request, 'base.html')

def member(request, username):
    member = User.objects.get(username=username)
    return render(request, 'member.html', {'member':member})

def events(request):
    return render(request, 'base.html')


