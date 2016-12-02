from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models
from suit_ckeditor.widgets import CKEditorWidget

from .models import Post, Comments

admin.site.unregister(User)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)


admin.site.register(User, CustomUserAdmin)


class PostInline(admin.StackedInline):
    model = Comments
    extra = 3


class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'created_date', 'published_date', 'image']
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    inlines = [PostInline]


admin.site.register(Post, PostAdmin)
