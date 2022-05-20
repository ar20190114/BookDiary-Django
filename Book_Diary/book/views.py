from django.db import models
from django.shortcuts import render
from .models import BookModel
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

# Create your views here.
class BookList(ListView):
    model = BookModel
    template_name = 'list.html'


class BookCreate(CreateView):
    model = BookModel
    template_name = 'create.html'
    success_url = reverse_lazy('list')
    fields = ('title', 'name', 'image', 'comment', 'endday')


class BookDelete(DeleteView):
    model = BookModel 
    template_name = 'delete.html'
    success_url = reverse_lazy('list')


class BookDetail(DetailView):
    model = BookModel
    template_name = 'detail.html'


class BookUpdate(UpdateView):
    model = BookModel
    template_name = 'update.html'
    success_url = reverse_lazy('list')
    fields = ('title', 'name', 'image', 'comment', 'endday')
