from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import MarketplaceDataSerializer
from .models import MarketplaceData
from .permissions import HasNFT


class Test(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"success": True})


# class BuyPack(APIView):
#     permission_classes = 0
#     pass


class MarketplaceDataViewSet(ModelViewSet):
    queryset = MarketplaceData.objects.filter(active=True)
    serializer_class = MarketplaceDataSerializer
    lookup_field = 'nft_token'
    # permission_classes = [AllowAny]

    def get_permissions(self):
        if not self.request.data:
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'delete':
            permission_classes = [HasNFT]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
