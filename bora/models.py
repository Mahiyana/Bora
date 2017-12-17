from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

class Rank(models.Model):
   name = models.TextField(verbose_name=_('Name'))
   def __str__(self):
        return self.name

def aliiki(instance, filename):
    return 'aliiki/{0}'.format(filename)

class User(AbstractUser):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    art_name = models.CharField(verbose_name=_('Art name'), max_length=255, null=True, blank=True)
    op_name = models.CharField(verbose_name=_('Operation name'), max_length=255, null=True, blank=True)
    aliik = ImageField(upload_to=aliiki, null=True, blank=True)
    story = models.TextField(verbose_name=_('Story'), null=True, blank=True)
    about = models.TextField(verbose_name=_('About'), null=True, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, null=True, blank=True)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('show_member', args=[self.username])


class ArticleCategory(models.Model):
   name = models.TextField(verbose_name=_('Name'))
   def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    content = models.TextField(verbose_name=_('Content'))
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('show_article', args=[self.id])

class Gallery(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    def __str__(self):
        return self.title

def user_gallery_path(instance, filename):
    return 'prace/{0}/{1}'.format(instance.user.username, filename)

class Artwork(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ImageField(upload_to=user_gallery_path)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('show_artwork', args=[self.id])

class Event(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    introduction = models.TextField(verbose_name=_('Introduction'))
    ending = models.TextField(verbose_name=_('Ending'))
    year = models.PositiveIntegerField(verbose_name=_('Year'))
    views = models.PositiveIntegerField(default=0)
    description = models.TextField(verbose_name=_('Description'))
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('event', args=[self.id])


class Report(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = ImageField(upload_to=aliiki, null=True, blank=True)
    report = models.TextField(verbose_name=_('Report'), null=True, blank=True)
