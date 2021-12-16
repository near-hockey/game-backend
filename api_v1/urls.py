from django.contrib import admin
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'test-endpoint/?', Test.as_view(), name="test"),
    re_path(r'nft/marketplace/?$', MarketplaceDataViewSet.as_view({'get': 'list',
                                                                  'post': 'create'}), name="marketplace"),
    re_path(r'nft/marketplace/(?P<nft_token>\d+)', MarketplaceDataViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    }), name="single-marketplace"),
    # re_path(r'buy-pack/?', BuyPack.as_view(), name='buy-pack'),
]
