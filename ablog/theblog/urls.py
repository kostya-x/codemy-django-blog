from django.urls import path
from .views import AddPostView, ArticleView, HomeView, AddPostView, EditPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('add/', AddPostView.as_view(), name="add"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit"),
]
