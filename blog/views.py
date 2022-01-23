from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def about(request):
    return render(request, 'blog/about.html')

def sustainability(request):
    return render(request, 'blog/sustainability.html')

def blog(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', context)

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()

            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/detail.html', context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'blog/category.html', {'category': category})


@login_required
def add_post(request):
    """ a view to add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('store'))

    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Successfully added blog post")
            return redirect(reverse('post_detail', args=[obj.slug]))
        else:
            messages.error(
                request, "Failed to add blog post, please check the form is valid")
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
