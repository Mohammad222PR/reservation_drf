from django.urls import path
from .. import views


urlpatterns = [
    path('activation/confrim', views.RegisterLoginSerializer.as_view(), name='activation-user'),
    path('activation/resend', views.ResendActivationEmailView.as_view(), name='activation-user-resend')
]
