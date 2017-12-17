from django.shortcuts import render, redirect
from .models import Article, Gallery, Artwork, User, Event, Report
from .forms import ArticleCategoryForm, ArticleForm, GalleryForm, ArtworkForm, UserForm, EventForm, ReportForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.urls import resolve 
from urllib.parse import urlparse

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
        gallery_id = resolve(urlparse(request.META['HTTP_REFERER']).path).kwargs['id']
        instance = Artwork(gallery_id=gallery_id)
        form =  ArtworkForm(instance=instance)
        #form.instance.gallery = Gallery.objects.get(id=gallery_id)
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
    members = User.objects.all()
    grouped_members = {}
    other = []
    for member in members:
        if member.rank is None:
          other.append(member)
          continue
        if member.rank.name not in grouped_members:
          grouped_members[member.rank.name] = []
        grouped_members[member.rank.name].append(member)
    if len(other) > 0:
        grouped_members['Inne'] = other
    return render(request, 'members.html', {'grouped_members': grouped_members})

def member(request, username):
    member = User.objects.get(username=username)
    return render(request, 'member.html', {'member':member})

@login_required
def edit_profile(request, username):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=User.objects.get(username=username))
        if form.is_valid():
            form.save()
            return redirect(form.instance)
    else:
        form = UserForm(instance=User.objects.get(username=username))
    return render(request, 'edit_profile.html', {'form': form})


def events(request, year):
    events = Event.objects.filter(year=year)
    years = Event.objects.order_by('year').distinct().values_list('year', flat=True) 
    return render(request, 'events.html', {'events': events, 'years': years})

def events_redirect(request):
    biggest_year = Event.objects.all().aggregate(Max('year'))['year__max']
    return redirect('events', year=biggest_year)

def event(request, id):
    event = Event.objects.get(id=id)
    reports= Report.objects.filter(event=event)
    user_wrote_report = False
    user_reports = Report.objects.filter(author=request.user).count()
    if user_reports > 0:
        user_wrote_report = True
    return render(request, 'event.html', {'event': event, 'reports': reports, 'user_wrote_report': user_wrote_report})

@login_required
def add_event(request):
    form = EventForm()
    if request.method == 'POST':
        print(request.POST)
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(form.instance)
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


@login_required
def edit_event(request, id):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=Event.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(form.instance)
    else:
        form = EventForm(instance=Event.objects.get(id=id))
    return render(request, 'edit_event.html', {'form': form})

@login_required
def add_report(request, event_id):
    form = ReportForm()
    if request.method == 'POST':
        print(request.POST)
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.event = Event.objects.get(id=event_id)  
            form.save()
            return redirect(form.instance.event)
    else:
        form =  ReportForm()
    return render(request, 'add_report.html', {'form': form})

@login_required
def edit_report(request, id):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=Report.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(form.instance.event)
    else:
        form = ReportForm(instance=Report.objects.get(id=id))
    return render(request, 'edit_report.html', {'form': form})
