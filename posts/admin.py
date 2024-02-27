from django.contrib import admin

# Register your models here.
from .models import Post
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created')  # Add other fields you want to display

admin.site.register(Post, PostAdmin)

