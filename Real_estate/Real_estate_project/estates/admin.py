from django.contrib import admin
from .models import Category, Post, Comment, Contact, Newsletter
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    #pass
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact)
admin.site.register(Newsletter)
