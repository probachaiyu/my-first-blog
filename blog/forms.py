from django import forms

from .models import Comments, Category, Tag
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('category','title', 'text', 'image','tag',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments_text',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

