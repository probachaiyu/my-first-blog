from django.conf.urls import url

from blog.views import BookList, AddComment, AddLike, PostTemplateView, PostEdit, PostDetailsView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', BookList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailsView.as_view(), name='post_detail'),
    url(r'^post/new/$', PostTemplateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', PostEdit.as_view(), name='post_edit'),
    url(r'^post/add_like/(?P<post_id>\d+)/$', AddLike.as_view(), name='post_like'),
    url(r'^post_detail/addcomment/(?P<post_id>\d+)/$', AddComment.as_view(), name='post_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
