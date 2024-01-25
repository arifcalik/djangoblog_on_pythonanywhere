from django.urls import path
from . import views
from .views import PostListView, PostUpdateView, UserPostListView, PostDeleteView, PostDetailView, PostCreateView
from .views import SearchResultsView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    
    path('post/new/', PostCreateView.as_view(), name='post-create'),    
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),    
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('about/', views.about, name='blog-about'),    
    path('post/post-like/<int:pk>', views.PostLike, name="post_like"),
]
