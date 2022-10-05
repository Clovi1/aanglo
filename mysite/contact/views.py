from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from blog.forms import UserEmailsForm
from .forms import *
from .models import *

menu = [{'title': 'home', 'url_name': 'home'},
        {'title': 'blog', 'url_name': 'blog'},
        {'title': 'about', 'url_name': 'about'},
        {'title': 'contact', 'url_name': 'contact'},
        ]


class CreateContact(CreateView):
    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Contact with me"
        context['menu_item_selected'] = "contact"
        context['email_form'] = UserEmailsForm()
        return context


# TODO: Singleton
class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        context = {'about': about,
                   'menu': menu,
                   'title': "About me",
                   'menu_item_selected': "about",
                   'email_form': UserEmailsForm(),
                   }
        return render(request, 'contact/about.html', context)
