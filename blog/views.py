from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.views.generic import ListView
from .models import Post, Category


def home(request):
	return HttpResponse('<h1>Home page is coming soon! :)</h1>')

def about(request):
	return HttpResponse('<h1>About page is coming soon! ;) </h1>')



class PostListView(ListView):
	model = Post
	template_name = 'blog/blog.html'

	must_read = Post.objects.filter(must_read=True)
	favorite = Post.objects.filter(favorite=True)
	context_object_name = 'posts'
	extra_context = {'must_read': must_read, 'favorite': favorite}
	
	ordering = ['-date_posted']
	paginate_by = 2



class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'

	must_read = Post.objects.filter(must_read=True)
	favorite = Post.objects.filter(favorite=True)
	context_object_name = 'posts'
	extra_context = {'must_read': must_read, 'favorite': favorite}
	
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')



class CategoryPostListView(ListView):
	model = Post
	template_name = 'blog/category_posts.html'

	must_read = Post.objects.filter(must_read=True)
	favorite = Post.objects.filter(favorite=True)
	context_object_name = 'posts'
	extra_context = {'must_read': must_read, 'favorite': favorite}
	
	paginate_by = 2

	def get_queryset(self):
		category = get_object_or_404(Category, name=self.kwargs.get('name'))
		return Post.objects.filter(category=category).order_by('-date_posted')




def postDetailView(request, pk):
	post = Post.objects.get(pk=pk)
	must_read = Post.objects.filter(must_read=True)
	favorite = Post.objects.filter(favorite=True)

	context = {'post': post, 'must_read': must_read, 'favorite': favorite}

	return render(request, 'blog/post_detail.html', context)



