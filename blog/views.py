from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

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


class PostDetailsView(TemplateView):
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        data = super().get_context_data(**kwargs)
        data['post'] = get_object_or_404(Post, pk=pk)
        data['username'] = auth.get_user(self.request).username
        data['comments'] = Comments.objects.filter(comments_post_id=pk)
        data['form'] = CommentForm
        return data


class PostTemplateView(FormView):
    template_name = 'post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('post_list')


class PostEdit(UpdateView):
    template_name = 'post_edit.html'
    model = Post
    form_class = PostForm

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('post_detail', args=(self.kwargs['pk'],))


class AddLike(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=pk)
        post.likes += 1
        post.save()
        return reverse('post_detail', args=(pk,))


class AddComment(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comments_post = Post.objects.get(id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=(self.kwargs['post_id'],))
