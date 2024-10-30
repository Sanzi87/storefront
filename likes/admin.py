from django.contrib import admin
from .models import LikedItem


@admin.register(LikedItem)
class LikedItemAdmin(admin.ModelAdmin):
    search_fields = ['label']
