from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Category, Post
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def about(request):
    """View to render the about us blog page """
    return render(request, 'blog/about.html')

def sustainability(request):
    """ View to render sustainability blog page """
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

            return redirect(
                'post_detail',
                
                slug=post.slug
            )
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

    form = PostForm()

    if request.method == "POST":
        try:
            post.slug = request.POST['title']
            post.save()

            messages.success(request, f'Successfully added {post.title}!')
            return redirect(reverse(
            'post_detail',
                slug=post.slug))
        except:
            messages.error(request, "Failed to add blog post, please ensure the form is valid")

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    ### Edit a post in blog ###
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this service is only for store owners')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated post: {post.title}!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, f'Failed to update post: {post.name}. Please ensure form is valid and try again.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing post: {post.name}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)

@login_required
def delete_post(request, post_slug):
    # Delete a post from the blog 
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this service is only for store owners')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, f'Post: {post.title} deleted!')
    return redirect(reverse('blog'))
