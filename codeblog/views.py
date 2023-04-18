from django.shortcuts import render
from codeblog.models import Category, Post
from codeblog.forms import CommentForm

# Create your views here.
def frontpageView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'frontpage.html', context)

def detailView(request, slug):
    post=Post.objects.get(slug=slug)
    form=CommentForm()
    context={
        'post_detail':post,
        'form_detail':form
    }
    return render(request,'detail.html', context)

def categoryView(request, slug):
    category=Category.objects.get(slug=slug)
    context={
        'category_pair':category
    }
    return render(request,'category.html', context)