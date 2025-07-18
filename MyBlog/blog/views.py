from django.shortcuts import render, get_object_or_404
from .models import Post, Author

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'post.html', {'post': post})

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-published_date')
    return render(request, 'author.html', {
        'author': author,
        'posts': posts
    })