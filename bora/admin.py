from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Article, User, ArticleCategory, Gallery, Artwork, Rank, Event, Report

admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(Gallery)
admin.site.register(Artwork)
admin.site.register(Rank)
admin.site.register(Event)
admin.site.register(Report)
