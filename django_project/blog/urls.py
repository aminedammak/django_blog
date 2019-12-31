from django.urls import path
from . import views
from .views import PostsListView, PostDetailView

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-home'),
    path('post-detail/<pk>', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about')
]