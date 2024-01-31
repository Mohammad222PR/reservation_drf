from rest_framework import serializers

from core.blog.models import Blog, Tag, Category


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tag = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Tag.objects.all())
    category = serializers.SlugRelatedField(slug_field='title', many=False, queryset=Category.objects.all())
    url_blog = serializers.SerializerMethodField(source='url_blog')
    images = serializers.SerializerMethodField(source='image_url')

    class Meta:
        model = Blog
        fields = '__all__'

    def get_url_post(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(obj.url)
        else:
            return None

    def get_images(self, obj):
        request = self.context.get('request', None)
        if obj.images:
            image = obj.images.url
            return request.build_absolute_uri(image)
        else:
            return None

    def to_representation(self, instance):
        request = self.context.get('request', None)
        rep = super().to_representation(instance)

        try:
            if request.parser_context.get('kwargs').get('pk'):
                rep.pop('url_post', None)

        except:
            return None
