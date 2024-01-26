from mail_templated import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from core.accounts.api.v1.serializers.register_login import *
from core.accounts.api.v1.utils import EmailSend
from core.accounts.models import User


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterLoginSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data.get('email')
            data = {
                'email': email
            }
            user = get_object_or_404(User, email=email)
            token = self.get_token_for_user(user=user)
            email_obj = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "admin@admin.com",
                to=[email],
            )
            EmailSend(email_obj).start()
            return Response(data={f'we send email to {data}'}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ResendActivationEmailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResendActivationEmailSSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        user = serializer.validated_data.get('user')
        token = self.get_token_for_user(user)
        email_obj = EmailMessage(
            "email/activation_email.tpl",
            {"token": token},
            "admin@admin.com",
            to=[user.email],
        )
        EmailSend(email_obj).start()
        return Response({'success': f'we are send email to {user.email}'}, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

