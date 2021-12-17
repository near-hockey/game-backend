from rest_framework.permissions import BasePermission
import near_api
from django.conf import settings


class HasNFT(BasePermission):
    def has_permission(self, request, view):
        provider = near_api.providers.JsonProvider(settings.NEAR_URL)
        account = near_api.account.Account(provider, None, request.data.get('user_id'))
        response = account.view_function(settings.CONTRACT, "nft_token", {
            "token_id": request.data.get('nft_token')
        })
        nft_data = response['result']
        if nft_data is None:
            return False
        if nft_data.get('owner_id') == request.data.get('user_id').strip():
            return True
        return False

