from django.urls import path

from .views import *

urlpatterns = [
    path('comment/<int:pk>', CreateComment.as_view(), name='create_comment'),
    path('email/', CreateUserEmails.as_view(), name='create_email'),
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogList.as_view(), name='blog'),
    path('tag/<slug:tag_slug>', TagList.as_view(), name='tag'),
    path('post/<slug:post_slug>/', PostDetail.as_view(), name='post'),
]