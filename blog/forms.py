from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    tag = forms.CharField()
    class Meta:
        model = Post
        fields = ('title', 'text',)

# class PostForm(forms.ModelForm):
#     title = forms.CharField()
#     text = forms.CharField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)