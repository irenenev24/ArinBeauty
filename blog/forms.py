from django.forms import ModelForm
from .models import Comment, Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'title', 'description']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'intro', 'content', 'author']
