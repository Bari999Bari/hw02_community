from django.shortcuts import render, get_object_or_404

from .models import Post, Group

LIMIT_ITEMS = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:LIMIT_ITEMS]
    context = {
        'posts': posts
    }
    return render(request, template, context)


# Posts sorted by group
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LIMIT_ITEMS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
