from django.shortcuts import render, redirect
from .models import Article, Gallery, Artwork, User, Event, Report, ReviewItem, ReviewCategory, Review
from .forms import ArticleCategoryForm, ArticleForm, GalleryForm, ArtworkForm, UserForm, EventForm, ReportForm, ReviewItemForm, ReviewForm
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
            form.instance.author = request.user
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
def delete_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('/artykuly')
    return render(request, 'delete_article.html', {'article': article})

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
            form.instance.author = request.user
            form.save()
            return redirect(form.instance.gallery)
    else:
        gallery_id = resolve(urlparse(request.META['HTTP_REFERER']).path).kwargs['id']
        instance = Artwork(gallery_id=gallery_id)
        form =  ArtworkForm(instance=instance)
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

@login_required
def delete_artwork(request, id):
    artwork = Artwork.objects.get(id=id)
    gallery = artwork.gallery
    if request.method == 'POST':
        artwork.delete()
        return redirect(gallery)
    return render(request, 'delete_artwork.html', {'artwork': artwork})

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
    user_reports = event.report_set.filter(author=request.user).count()
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
            form.instance.author = request.user
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

def whole_review(request, id):
    review_item = ReviewItem.objects.get(id=id)
    reviews= Review.objects.filter(item=review_item)
    user_wrote_review = False
    user_reviews = Review.objects.filter(author=request.user).count()
    if user_reviews > 0:
        user_wrote_review = True
    return render(request, 'whole_review.html', {'review_item': review_item, 'reviews': reviews, 'user_wrote_review': user_wrote_review})

@login_required
def add_review_item(request):
    form = ReviewItemForm()
    if request.method == 'POST':
        print(request.POST)
        form = ReviewItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(form.instance)
    else:
        form =  ReviewItemForm()
    return render(request, 'add_review_item.html', {'form': form})

@login_required
def edit_review_item(request, id):
    form = ReviewItemForm()
    if request.method == 'POST':
        form = ReviewItemForm(request.POST, request.FILES, instance=ReviewItem.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(form.instance)
    else:
        form =  ReviewItemForm(instance=ReviewItem.objects.get(id=id))
    return render(request, 'edit_review_item.html', {'form': form})

def reviews(request):
    reviews = ReviewItem.objects.all()
    grouped_reviews = {}
    for review in reviews:
        if review.category is None:
          continue
        if review.category.name not in grouped_reviews:
          grouped_reviews[review.category.name] = []
        grouped_reviews[review.category.name].append(review)
    return render(request, 'reviews.html', {'grouped_reviews': grouped_reviews})

@login_required
def add_review(request):
    form = ReviewForm()
    if request.method == 'POST':
        print(request.POST)
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(form.instance.item)
    else:
        review_item_id = resolve(urlparse(request.META['HTTP_REFERER']).path).kwargs['id']
        instance = Review(item=ReviewItem.objects.get(id=review_item_id))
        form =  ReviewForm(instance=instance)
    return render(request, 'add_review.html', {'form': form})

@login_required
def edit_review(request, id):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=Review.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(form.instance.item)
    else:
        form =  ReviewForm(instance=Review.objects.get(id=id))
    return render(request, 'edit_review.html', {'form': form})


