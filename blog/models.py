from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogimages', null=True, blank=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", default=1)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.post.title, self.name)
