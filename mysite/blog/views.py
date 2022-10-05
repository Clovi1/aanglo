from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.models import *
from blog.forms import *

menu = [{'title': 'home', 'url_name': 'home'},
        {'title': 'blog', 'url_name': 'blog'},
        {'title': 'about', 'url_name': 'about'},
        {'title': 'contact', 'url_name': 'contact'},
        ]


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "AAnglo - Personal Blog"
        context['menu_item_selected'] = "home"
        context['email_form'] = UserEmailsForm()
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True) \
            .select_related('tag', 'author') \
            .only('title', 'slug', 'image', 'time_create', 'tag__name', 'author__username')


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.filter(is_published=True) \
        .select_related('tag', 'author') \
        .only('title', 'slug','content', 'image', 'time_create', 'tag__name', 'author__username')
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Post"
        context['form'] = CommentForm()
        context['email_form'] = UserEmailsForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CreateUserEmails(CreateView):
    model = UserEmails
    form_class = UserEmailsForm
    success_url = reverse_lazy('home')


class BlogList(ListView):
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Blog"
        context['menu_item_selected'] = "blog"
        context['email_form'] = UserEmailsForm()
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True) \
            .select_related('author') \
            .only('title', 'slug', 'content', 'image', 'time_create', 'author__username')


class TagList(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/tags.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = self.kwargs['tag_slug']
        context['menu_item_selected'] = "blog-masonry"
        context['email_form'] = UserEmailsForm()
        return context

    def get_queryset(self):
        return Post.objects.filter(tag__slug=self.kwargs['tag_slug'], is_published=True) \
            .select_related('tag', 'author') \
            .only('title', 'slug', 'image', 'time_create', 'tag__name', 'author__username')


def pageNotFound(request, exception):
    return render(request, 'blog/404.html')
