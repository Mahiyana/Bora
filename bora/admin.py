from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Article, User, ArticleCategory

admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(ArticleCategory)
