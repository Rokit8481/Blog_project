from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Comment

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'post_list.html', {
        'posts': posts
    })


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_date')
    return render(request, 'post.html', {
        'post': post,
        'comments': comments
    })

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-published_date')
    comments = Comment.objects.filter(author=author).order_by('-created_date')
    return render(request, 'author.html', {
        'author': author,
        'posts': posts,
        'comments': comments
    })
