# -*- coding: utf-8 -*-


from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts':posts})



def post_detail (request,post_number):

    post = get_object_or_404 (Post ,pk = post_number)
   
    return render(request, 'blog/post_detail.html', {'post':post})



def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
