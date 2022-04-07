from django.shortcuts import render
from .models import Blogs

def all_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
