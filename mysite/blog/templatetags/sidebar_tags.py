from django import template
from blog.models import Tags, Post

register = template.Library()


@register.inclusion_tag('blog/include/tags/sidebar.html')
def get_sidebar():
    posts = Post.objects.filter(is_published=True) \
                .order_by("-time_create") \
                .only('title', 'slug', 'image', 'time_create')[:3]
    tags = Tags.objects.all()
    return {'posts': posts,
            'tags': tags}
