from blog.models import Post
from django.shortcuts import render_to_response
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
	title = "Django PIP Blog"
	description = "Git your learn on..."
	link = "/blog/feed/"

	def items(self):
		return Post.objects.all().order_by("-created")[:2]
	def item_title(self, item):
		return item.title
	def item_description(self, item):
		return item.body
	def item_link(self, item):
		return u"/blog/%d" % item.id

def tagpage(request, tag):
	posts = Post.objects.filter(tags__name=tag)
	return render_to_response("tagpage.html", {"posts":posts, "tag":tag})
