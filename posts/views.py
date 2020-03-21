from django.shortcuts import render
from django.views.generic import ListView
from .models import Post



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_list'
