from django.urls import path
from . import views
from .views import PostsListView, PostDetailView, PostDeleteView, PostCreateView

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-home'),
    path('post-detail/<pk>', PostDetailView.as_view(), name='post-detail'),
    path('post-delete/<pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]