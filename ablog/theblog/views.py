from dataclasses import fields
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import AddForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddForm
    template_name = 'add.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
