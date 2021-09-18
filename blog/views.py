from re import template
from django.db.models.query_utils import Q
from .models import Category, Post 
from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from django.db.models import Count
from taggit.models import Tag
# Create your views here.
class Posts(ListView):
    model=Post
    paginate_by=2

    def get_queryset(self):
        name=self.request.GET.get('q','')
        
        object_list=Post.objects.filter(
            
            Q(title__icontains=name) |
            Q(discription__icontains=name)
            )
        return object_list
    
    


class Post_detail(DetailView):
    model=Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent"] = Post.objects.all()[:3]
        context['category'] = Category.objects.all().annotate(post_count = Count('post_category'))
        context['tags'] = Tag.objects.all()

        return context

class PostByCategory(ListView):
    model=Post
    # template_name='blog/post_list.html'
    def get_queryset(self):
        slug=self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains = slug )
        )
        return object_list


class PostByTags(ListView):
    model=Post
    def get_queryset(self):
        slug=self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(tags__name__icontains = slug )
        )
        return object_list
    


    