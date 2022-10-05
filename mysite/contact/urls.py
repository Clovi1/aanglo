from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('about/', cache_page(60 * 60 * 24 * 7)(AboutView.as_view()), name='about'),
    path('contact/', CreateContact.as_view(), name='contact'),
]