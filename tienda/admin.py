from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ['name', 'pvp', 'author', 'publish', 'status']
 list_filter = ['status', 'created', 'publish', 'author']
 search_fields = ['name', 'body']
 prepopulated_fields = {'pvp': ('title',)}
 raw_id_fields = ['author']
 date_hierarchy = 'publish'
 ordering = ['status', 'publish']