from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny


class Test(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"success": True})
