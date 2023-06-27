from django.contrib import admin
from .models import Keywords, Links, Info


@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'status')


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'reviews', 'characteristic1', 'characteristic2', 'characteristic3', 'characteristic4', 'characteristic5')
