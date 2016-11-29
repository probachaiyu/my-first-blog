from django.contrib import admin
from .models import Post, Comments

admin.site.register(Post)

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin    

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff','is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)    
admin.site.register(User, CustomUserAdmin)

class PostInline(admin.StackedInline):
    model = Comments
    extra =2

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text','created_date', 'published_date']
    inlines = [PostInline]

admin.site.unregister(Post)
admin.site.register(Post, PostAdmin)
