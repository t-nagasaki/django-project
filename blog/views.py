from django.shortcuts import render
from django.views import generic
from blog.models import Entry

# Create your views here.

class DetailView(generic.DetailView):
    model=Entry
    template_name = 'blog/detail.html'
