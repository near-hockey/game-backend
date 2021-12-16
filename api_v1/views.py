from django.shortcuts import render
from rest_framework.views import APIView, Response


class Test(APIView):
    def get(self, request):
        return Response({"success": True})
