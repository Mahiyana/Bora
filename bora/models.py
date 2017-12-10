from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


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
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
