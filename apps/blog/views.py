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
		context['post_featured'] = Post.objects.filter(post_type='featured').order_by('id')[0:1]
		# Load post by featured
		context['post_editor_pick_1'] = Post.objects.filter(is_editor_pick=True).order_by('id')[0:1]
		# Load post by featured
		context['post_editor_pick_4'] = Post.objects.filter(is_editor_pick=True).order_by('id')[1:5]
		# Load post by trending
		context['post_trending_large_1'] = Post.objects.filter(is_trending=True).order_by('id')[0:1]
		# Load post by trending
		context['post_trending_small_2'] = Post.objects.filter(is_trending=True).order_by('id')[1:3]
		# Load post by trending
		context['post_trending_large_1_1'] = Post.objects.filter(is_trending=True).order_by('id')[3:4]
		# Load post by trending
		context['post_trending_small_2_2'] = Post.objects.filter(is_trending=True).order_by('id')[4:6]
		# Page title
		context['title'] = 'Blog Magazine'
		return context


def PostSingle(request):
	return render(request, 'blog/post_single.html')


def About(request):
	return render(request, 'blog/about.html')


def Contact(request):
	return render(request, 'blog/contact.html')