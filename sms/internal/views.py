from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

from .forms import BlogForm
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'internal/template/blog_list.html', {'blogs': blogs})
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog created successfully')
            return redirect('blog_list')
        else:
            messages.error(request, 'There was an error creating the blog')
    else:
        form = BlogForm()
    return render(request, 'internal/template/blog_form.html', {'form': form})

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully')
            return redirect('blog_list')  # Update this to your blog list URL name
        else:
            messages.error(request, 'There was an error updating the blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'internal/template/update_blog.html', {'form': form, 'blog': blog})


def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted successfully')
        return redirect('blog_list')
    #return render(request, 'internal/template/blog_list.html', {'blog': blog})
