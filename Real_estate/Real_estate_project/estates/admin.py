from django.contrib import admin
from .models import Category, Post, Comment, Contact, Newsletter, Property, PropertyContact, UserVisit
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    
class CommentAdmin(admin.ModelAdmin):
    pass

class PropertyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Newsletter)
admin.site.register(PropertyContact)
admin.site.register(UserVisit)
