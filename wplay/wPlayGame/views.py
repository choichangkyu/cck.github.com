from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def index_html(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, "wPlayGame/index.html", {'posts' : posts})

def about_html(request):
    return render(request, "wPlayGame/about.html")

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, "wPlayGame/post_list.html", {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('wPlayGame.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'wPlayGame/post_detail.html', {'post': post, 'form':form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.now()
            post.save()
            return redirect('wPlayGame.views.post_detail', pk = post.pk)
    else:
        form = PostForm()
        
    return render(request, 'wPlayGame/post_new.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.pk = post_id
            post.published_date = timezone.now()
            post.save()
            return redirect('wPlayGame.views.post_detail', pk = post.pk)

    else:
        form = PostForm(instance = post)

    return render(request, 'wPlayGame/post_edit.html', {'form':form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'wPlayGame/post_draft_list.html', {'posts' : posts})

def post_publish(request, post_id):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('wPlayGame.views.post_detail', pk = pk)

def post_remove(request, post_id):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('wPlayGame.views.post_list')

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('wPlayGame.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('wPlayGame.views.post_detail', pk=post_pk)

def approved_comments(self):
    return self.comments.filter(approved_comment=True)

