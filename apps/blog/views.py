# apps/blog/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import ListView

# Locals
from apps.blog.models import Post  

# Create your views here.


# CLASS VIEW: Home
class PostList(ListView):
	model 				= Post 
	template_name 		= 'blog/post_list.html'
	context_object_name = 'post_list'

	def get_context_data(self, **kwargs):
		
		# To get contex, first, call base implementation
		context = super().get_context_data(**kwargs)

		# GET POST BY POST_TYPE

		# Load post by featured
		context['post_featured'] = Post.objects.filter(post_type='featured')
		# Page title
		context['title'] = 'Blog Magazine'
		return context


def PostSingle(request):
	return render(request, 'blog/post_single.html')


def About(request):
	return render(request, 'blog/about.html')


def Contact(request):
	return render(request, 'blog/contact.html')