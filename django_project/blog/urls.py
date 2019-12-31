from django.urls import path
from . import views
from .views import PostsListView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-home'),
    path('post-detail/<pk>', PostDetailView.as_view(), name='post-detail'),
    path('post-delete/<pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('post-update/<pk>', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about')
]