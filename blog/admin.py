from django.contrib import admin
from blog.models import Post, Tag, Comment
# Register your models here.

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  populated_fields = {"slug": ("title",)}
  list_display = ('summary', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)