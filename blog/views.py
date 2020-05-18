from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy

# Create your views here. 
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    #Pythonic way of writing sql query (ORM)
    def get_queryset(self):
        #Grab the posts where published date is less than or equal to current timezone
        #order by published_date
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date_isnull=True).order_by('created_date')
