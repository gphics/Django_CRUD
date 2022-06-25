from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
    
# Create your views here.
class PostListView(ListView):
    template_name = "post_list.html"
    model = Post
class PostCreateView(CreateView):
    template_name = "post_form.html"
    model = Post
    fields ="__all__"
    url  = reverse_lazy("blog:all")
    
class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model =  Post
    
class PostUpdateView(UpdateView):
    template_name = "post_list.html"
    model = Post
    fields ="__all__"
    url  = reverse_lazy("blog:all")
    
class PostDeleteView(UpdateView):
    template_name = "post_confirm_delete.html"
    model = 'Post'
    fields ="__all__"
    url  = reverse_lazy("blog:all")
    
    

