from django.shortcuts import render
from blog.models import Post
from blog.models import Bloglist
# Create your views here.

def index(request):
	posts=Post.objects.filter(published=True)
	bloglists=Bloglist.objects.filter(published1=True)
	requestlist={'posts':posts,'bloglists':bloglists}
	return render(request,'blog/index.html',requestlist)

def post(request,slug):
	post=get_object_or_404(Post,slug=slug)
	return render(request,'blog/post.html',{'post':post})