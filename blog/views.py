from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator


# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date')
#     return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


def posts_list(request):
    posts = Blog.objects.all().order_by('-date')
    how_much_posts_all = posts.count()
    how_much_posts = 2
    paginator = Paginator(posts, how_much_posts)
    page_number = request.GET.get('page', default=1)
    page = paginator.get_page(page_number)

    return render(request, 'blog/all_blogs.html', {'posts': page, 'pag': how_much_posts_all, 'pag_2': how_much_posts})
