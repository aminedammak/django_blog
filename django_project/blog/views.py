from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = Post.objects.all()


def home(request):
    return render(request, 'index.html', {"posts": posts})


def about(request):
    return HttpResponse("<h2>About</h2>")