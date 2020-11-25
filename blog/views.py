from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def ShowBlog(request):
	posts = Post.objects
	return render(request,r"blog\blog.html",{'posts': posts})

def specific_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request,r"blog\specific_post.html",{'post': post})
