from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.
class PostView(generic.ListView):
    template_name = 'blog/posts.html'
    model = Post


# Para mostrar un unico post hay la siguiente generic
class PostDetailView(generic.DetailView):
    template_name = "blog/detail.html"
    model = Post

# Para que el usario pueda agregar un post
class NewPostView(generic.CreateView):
    template_name = 'blog/post_new.html'
    model = Post
    fields = ['title', 'author', 'text']
    success_url = "/blog/posts/"