from django.urls import path

from core.blog.api.v1 import views

urlpatterns = [
    path('list', views.BlogListAndPostView.as_view(), name='blog_list'),
    path('detail', views.BlogRetrivAndUpdateView.as_view(), name='blog_detail')
]