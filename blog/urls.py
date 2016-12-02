from django.conf.urls import url

from blog.views import BookList
from . import views

urlpatterns = [
    url(r'^$', BookList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/add_like/(?P<post_id>\d+)/$', views.post_like, name='post_like'),
    url(r'^post_detail/addcomment/(?P<post_id>\d+)/$', views.post_comment, name='post_comment'),
]
