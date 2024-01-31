from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.api.v1.serializers.change_pass import ChangePasswordSerializer
from accounts.models import User


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
