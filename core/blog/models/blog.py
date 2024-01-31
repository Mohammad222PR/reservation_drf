from django.db import models
from ckeditor.fields import RichTextField

from core.accounts.models import User
from core.blog.validators import *


class Tag(models.Model):
    title = models.CharField(max_length=100, validators=[validate_tag_title])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    title = models.CharField(max_length=100, validators=[validate_tag_title])
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    child = models.ForeignKey('self', on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=1000, validators=[validate_blog_title])
    slug = models.SlugField(max_length=1000, validators=[validate_blog_slug])
    content = RichTextField(validators=[validate_blog_content])
    images = models.ImageField(upload_to='image/blogs/photo', validators=[validate_file_image])
    tag = models.ManyToManyField(Tag, blank=True, null=True, validators=[validate_tag_title],
                                 related_query_name='blog')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs',
                                 validators=[validate_category_title])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models, related_name='comments')
    title = models.CharField(max_length=1000, validators=[validate_blog_title])
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_query_name='comments')
    comment = models.TextField(max_length=2000, validators=[validate_blog_content])
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
