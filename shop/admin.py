from django.contrib import admin
from shop.models import(FishCategory,
                        Seller,
                        Contact,
                        SellerPost,
                        SellerInbox,
                        Newsletter,
                        )


class FishAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}

    class Meta:
        model = FishCategory
admin.site.register(FishCategory, FishAdmin)


class SellerAdmin(admin.ModelAdmin):
    list_display = ['seller_username', 'phone_no', 'location']

    class Meta:
        model = Seller
admin.site.register(Seller, SellerAdmin)


class SellerPostAdmin(admin.ModelAdmin):
    list_display = ['seller',
                    'fish_category',
                    'quantity',
                    'price',
                    'available_amt',
                    'is_available',
                    'fish_photo',
                    ]

    class Meta:
        model = SellerPost
admin.site.register(SellerPost, SellerPostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'full_name', 'location']

    class Meta:
        model = Contact
admin.site.register(Contact, ContactAdmin)


class SellerInboxAdmin(admin.ModelAdmin):
    list_display = ['customer_phone',
                    'seller_phone',
                    'fish_category',
                    'price_per_kg',
                    'amount_requested',
                    'message_sent',
                    'date_sent'
                    ]

    class Meta:
        model = SellerInbox
admin.site.register(SellerInbox, SellerInboxAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']

    class Meta:
        model = Newsletter
admin.site.register(Newsletter, NewsletterAdmin)
