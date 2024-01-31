from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from core.blog.api.v1.pageination import *
from core.blog.api.v1.serializers import BlogSerializer
from core.blog.models import Blog
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60), name="get")
class BlogListAndPostView(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.filter(is_published=True)
    pagination_class = BlogPageination
    django_filters = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'tag', 'is_published', 'category']
    search_fields = ['title', 'author']
    ordering_fields = ['is_published']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, is_published=True)


class BlogRetrivAndUpdateView(APIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None):
        blog = get_object_or_404(Blog, id=pk)
        serializer = self.serializer_class(blog, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        blog = get_object_or_404(Blog, id=pk)
        serializer = self.serializer_class(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'success'}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()
        return Response(data={'detail': 'blog deleted successfully'}, status=status.HTTP_200_OK)
