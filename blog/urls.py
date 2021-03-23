from django.urls import path
from . import views
from .views import PostListView, postDetailView, UserPostListView, CategoryPostListView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'blog-about'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('blog/user/<str:username>/', UserPostListView.as_view(), name='blog-user-posts'),
    path('blog/category/<str:name>/', CategoryPostListView.as_view(), name='blog-category-posts'),
    path('blog/posts/<int:pk>/', views.postDetailView, name = 'blog-post-detail'),
]

