from rest_framework import serializers
from .models import MarketplaceData


class MarketplaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceData
        fields = 'nft_token', 'user_id', 'price', 'created'
