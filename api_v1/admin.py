from django.contrib import admin
from .models import MarketplaceData


@admin.register(MarketplaceData)
class MarketplaceDataAdmin(admin.ModelAdmin):
    list_display = 'nft_token', 'user_id', 'price', 'active', 'created'
