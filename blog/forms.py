from .models import Comment, Post
from django import forms

from tinymce.widgets import TinyMCE


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class add_blog_form(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'author')
