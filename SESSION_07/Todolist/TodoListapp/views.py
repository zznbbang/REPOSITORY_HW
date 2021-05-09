from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title= request.POST['title'],
            content=request.POST['content'],
            date=request.POST['date']
        )
        return redirect('detail', new_post.pk)

    return render(request,'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
    post=Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title= request.POST['title'],
            content=request.POST['content'],
            date=request.POST['date']
        )
        return redirect('detail', post.pk)

    return render(request,'edit.html',{'post':post})

def delete(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    post.delete()

    return redirect("home")