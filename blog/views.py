from django.shortcuts import render, redirect

from .models import Category, Post
from .forms import CommentForm

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

def detail(request, slug):
    post = Post.objects.get(slug=slug)

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


