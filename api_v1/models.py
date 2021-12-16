from django.db import models


class MarketplaceData(models.Model):
    nft_token = models.CharField("NFT", max_length=256)
    user_id = models.CharField("User id", max_length=128)
    created = models.DateTimeField("Date created", auto_now=True)
    price = models.FloatField("Price")
    active = models.BooleanField("Is active", default=True)

