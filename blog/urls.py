from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.views import BlogFeed

urlpatterns = patterns('blog.views',
  url(r'^$', ListView.as_view(
        queryset=Post.objects.order_by("-created"),
        context_object_name="posts")),
  url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Post)),
  url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
  url(r'^feed/$', BlogFeed()),
)
