from django.urls import path
from .. import views

urlpatterns = [
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),

]
