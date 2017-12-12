from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

class User(AbstractUser):
    pass

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
