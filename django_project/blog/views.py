from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView

posts = Post.objects.all()


def home(request):
    return render(request, 'index.html', {"posts": posts})


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
    ordering = ("-date_posted")


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"

def about(request):
    return HttpResponse("<h2>About</h2>")