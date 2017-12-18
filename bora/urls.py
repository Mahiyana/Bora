"""bora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    
    path('artykuly', views.articles, name='articles'),
    path('dodaj_artykul', views.add_article, name='add_article'),
    path('edytuj_artykul/<int:id>/', views.edit_article, name='edit_article'),
    path('usun_artykul/<int:id>/', views.delete_article, name='delete_article'),
    path('artykul/<int:id>/', views.article, name='show_article'),
    path('dodaj_kategorie', views.add_article_category),
    
    path('galerie', views.galleries, name='galleries'),
    path('galeria/<int:id>/', views.gallery, name='show_gallery'),
    path('dodaj_galerie', views.add_gallery, name='add_gallery'),
    path('edytuj_galerie/<int:id>/', views.edit_gallery, name='edit_gallery'),
    path('dodaj_prace', views.add_artwork, name='add_artwork'),
    path('praca/<int:id>/', views.artwork, name='show_artwork'),
    path('edytuj_prace/<int:id>/', views.edit_artwork, name='edit_artwork'),
    path('usun_prace/<int:id>/', views.delete_artwork, name='delete_artwork'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('czlonkowie', views.members, name='members'),
    path('czlonek/<str:username>/', views.member, name='show_member'),
    path('edytuj_profil/<str:username>/', views.edit_profile, name='edit_profile'),
    
    path('wydarzenia/<int:year>', views.events, name='events'),
    path('wydarzenia', views.events_redirect, name='events_redirect'),
    path('dodaj_wydarzenie', views.add_event, name='add_event'),
    path('wydarzenie/<int:id>', views.event, name='event'),
    path('edytuj_wydarzenie/<int:id>', views.edit_event, name='edit_event'),
    path('dodaj_relacje/<int:event_id>', views.add_report, name='add_report'),
    path('edytuj_relacje/<int:id>', views.edit_report, name='edit_report'),
    
    path('recenzja/<int:id>', views.whole_review, name='whole_review'),
    path('dodaj_pozycje_do_recenzji', views.add_review_item, name='add_review_item'),
    path('edytuj_pozycje_do_recenzji/<int:id>', views.edit_review_item, name='edit_review_item'),
    path('recenzje', views.reviews, name='reviews'),
    path('dodaj_recenzje', views.add_review, name='add_review'),
    path('edytuj_recenzje/<int:id>', views.edit_review, name='edit_review'),

    path('edytuj_newsa/<int:id>/', views.edit_news, name='edit_news'),
    path('usun_newsa/<int:id>/', views.delete_news, name='delete_news'),
    path('news/<int:id>/', views.news, name='news'),
    path('dodaj_newsa', views.add_news, name='add_news'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
