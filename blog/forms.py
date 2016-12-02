from django import forms

from .models import Comments
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments_text',)
