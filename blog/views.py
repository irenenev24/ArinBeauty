from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def about(request):
    ### View to render the about us blog page ###
    return render(request, 'blog/about.html')

def sustainability(request):
    ### View to render sustainability blog page ###
    return render(request, 'blog/sustainability.html')

def blog(request):
    ### View to render the main blog page ###
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', context)

def detail(request, category_slug, slug):
    ### View to render the blog page with the posts ###
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/detail.html', context)

def category(request, slug):
    ### View to render the blog category page ###
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'blog/category.html', {'category': category})


@login_required
def add_post(request):
    ### a view to add a post to the blog ###
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    if request.method == "POST":
        form = Post(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Successfully added blog post")
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, "Failed to add blog post, please check the form is valid")
    else:
        form = Post()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
