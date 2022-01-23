from django.forms import ModelForm

from .models import Comment, Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'description']

class PostForm():
    class Meta:
        model = Post
        fields = ['name', 'description']
