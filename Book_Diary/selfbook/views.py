from django.db import models
from django.shortcuts import render
from.models import SelfBookModel
from django.views.generic import ListView

# Create your views here.
class SelfbookList(ListView):
    models = SelfBookModel
    template_name = 'selfbooklist.html'