from dataclasses import fields
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import AddForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddForm
    template_name = 'add.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit.html'
    fields = ['title', 'subtitle', 'body']
