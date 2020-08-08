from django.contrib import admin
from .models import MyDiary


class DiaryIndex(admin.ModelAdmin):
    list_display = ['date_add', 'name', 'title', 'value', 'status']


admin.site.register(MyDiary, DiaryIndex)
