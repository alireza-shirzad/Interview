from django.urls import path, include
from blog.api.views import PostListView, RatingCreateView

urlpatterns = [
    path('posts',  PostListView.as_view()),
    path('rating', RatingCreateView.as_view())
]