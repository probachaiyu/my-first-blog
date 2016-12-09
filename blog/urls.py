from django.conf.urls import url

from blog.views import BookList, AddComment, AddLike, PostTemplateView, PostEdit, PostDetailsView, CommentEdit, \
    CommentDelete, TagView,  PostCategoryView, CategoryView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#url(r'^page/(?P<page>\d+)/$', PrivatePostList.as_view()),
    url(r'^$', BookList.as_view(context_object_name='posts'), name='post_list'),
    #url(r'^(?:(?P<page>\d+)/)?$', BookList.as_view(context_object_name='posts'), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailsView.as_view(), name='post_detail'),
    url(r'^post/new/$', PostTemplateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', PostEdit.as_view(), name='post_edit'),
    url(r'^post/add_like/(?P<post_id>\d+)/$', AddLike.as_view(), name='post_like'),
    url(r'^post_detail/addcomment/(?P<post_id>\d+)/$', AddComment.as_view(), name='post_comment'),
    url(r'^post_detail/(?P<pk>\d+)/edit_comment/(?P<id>\d+)/$', CommentEdit.as_view(), name='edit_comment'),
    url(r'^post_detail/(?P<pk>\d+)/delete_comment/(?P<id>\d+)/$', CommentDelete.as_view(), name='delete_comment'),
    url(r'^category/(?P<id>.*)/$', PostCategoryView.as_view() ,name ='category'),
    url(r'^post/(?P<pk>[0-9]+)/category/(?P<id>.*)/$', PostCategoryView.as_view() ,name ='category'),
    url(r'^tag/(?P<id>\d+)/$', TagView.as_view(), name = 'tag'),
    url(r'^post/(?P<pk>[0-9]+)/tag/(?P<id>\d+)/$', TagView.as_view(), name = 'tag'),
    url(r'^categories/$', CategoryView.as_view(), name = 'category_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
