from django import forms
from django.forms.models import ModelForm

from .models import Comments
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        #ordering = ['-published_date']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments_text',)
