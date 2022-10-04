from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'title',
        'blog',
        'date_posted',
    )
    exclude = ['id']

admin.site.register(Post, PostAdmin)