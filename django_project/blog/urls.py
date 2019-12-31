from django.urls import path
from . import views
from .views import PostsListView

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about')
]