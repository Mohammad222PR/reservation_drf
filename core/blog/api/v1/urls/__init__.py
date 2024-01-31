from .blog import *
from django.urls import include, path

app_name = 'api-v1'

urlpatterns = [
    path('blog/', include('blog.api.v1.urls.blog'))

]