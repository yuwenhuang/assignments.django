from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post
from .forms import PostForm

def index(request):
    return render(request,'blogs/index.html',locals()) 

# show all blog posts, order by descending date order
def post_list(request):
    # negative sign in front of "-published_date" indicates descending order
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blogs/post_list.html',{'posts':posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'New user is created. Please login')
            # after successful registration, redirect to index page
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form,})

#def registerok(request):
#    return render(request,'registration/registerok.html',locals()) 

#@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blogs/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_edit.html', {'form': form})