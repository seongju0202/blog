from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})

def detail(request, admin):
    blog_detail = get_object_or_404(Blog, pk=admin)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

