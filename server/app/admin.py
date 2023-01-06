from django.contrib import admin

from app.models import Menu, Post


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug':  ('title',)}
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    prepopulated_fields = {'slug':  ('title',)}
    empty_value_display = '-пусто-'
