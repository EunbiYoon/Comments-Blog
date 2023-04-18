from django.shortcuts import render,redirect
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

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post=post
            obj.save()
            return redirect('detail_url',slug=post.slug)
    else:
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