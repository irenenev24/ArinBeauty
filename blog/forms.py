from django.forms import ModelForm

from .models import Comment, Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'title', 'description']

class Post():
    class Meta:
        model = Post
        fields = ['name', 'image', 'description']
