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
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    path('artykuly', views.articles),
    path('dodaj_artykul', views.add_article),
    path('artykul/<int:id>/', views.article, name='show_article'),
    path('dodaj_kategorie', views.add_article_category),
    path('galerie', views.galleries),
    path('galeria/<int:id>/', views.gallery, name='show_gallery'),
    path('dodaj_galerie', views.add_gallery),
    path('edytuj_galerie/<int:id>/', views.edit_gallery, name='edit_gallery'),
    path('dodaj_prace', views.add_artwork),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
