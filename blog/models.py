from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Category(models.Model):
    title = models.CharField(max_length=255) 
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    intro = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", default=1)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    title = models.CharField(max_length=20, unique=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.post.title, self.name)

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.title + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=Post)
