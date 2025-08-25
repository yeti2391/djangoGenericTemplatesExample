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