from rest_framework.views import APIView
from rest_framework.response import Response


class Index(APIView):
    def get(self, request):
        return Response("hi")
