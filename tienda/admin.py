from django.contrib import admin
from .models import Post
from .models import Articulo
# Register your models here.
admin.site.register(Post)
admin.site.register(Articulo)
class PostAdmin(admin.ModelAdmin):
 list_display = ['name', 'pvp', 'author', 'publish', 'status']
 list_filter = ['status', 'created', 'publish', 'author']
 search_fields = ['name', 'body']
 prepopulated_fields = {'pvp': ('title',)}
 raw_id_fields = ['author']
 date_hierarchy = 'publish'
 ordering = ['status', 'publish']