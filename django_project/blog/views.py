from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return HttpResponse("<h2>About</h2>")