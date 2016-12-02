from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.utils import timezone
from django.views.generic import ListView

from .forms import CommentForm
from .forms import PostForm
from .models import Post, Comments


class BookList(ListView):
    queryset = Post.objects.order_by('-published_date')
    context_object_name = 'book_list'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['username'] = auth.get_user(self.request).username
        return data


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['post'] = post
    args['username'] = auth.get_user(request).username
    args['comments'] = Comments.objects.filter(comments_post_id=pk)
    args['form'] = comment_form
    return render(request, 'post_detail.html', args)


def post_new(request):
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_like(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def post_comment(request, post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_post = Post.objects.get(id=post_id)
            form.save()
    return redirect("/post/%s/" % post_id)
