from rest_framework.serializers import ModelSerializer

from shop.models import (Seller,
                         SellerPost,
                         FishCategory,
                         SellerInbox,
                         Newsletter,
)
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class SellerSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Seller
        fields = ('pk', 'user', 'phone_no', 'location', 'times_contacted')


class FishCategorySerializer(ModelSerializer):
    class Meta:
        model = FishCategory
        fields = ('id', 'category_name', 'slug')


class SellerPostSerializer(ModelSerializer):
    seller = SellerSerializer()
    fish_category = FishCategorySerializer()

    class Meta:
        model = SellerPost
        fields = ('id',
                  'seller',
                  'fish_category',
                  'fish_photo',
                  'quantity',
                  'price',
                  'available_amt',
                  'is_available',
                  'date_posted')


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'email')


class SellerInboxSerializer(ModelSerializer):
    class Meta:
        model = SellerInbox
        fields = (
            'id',
            'customer_phone',
            'seller_phone',
            'fish_category',
            'price_per_kg',
            'amount_requested',
            'message_sent',
            'date_sent'
        )



