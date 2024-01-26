from rest_framework.views import APIView

from core.accounts.api.v1.serializers.change_pass import ChangePasswordSerializer


class ChangePasswordView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
