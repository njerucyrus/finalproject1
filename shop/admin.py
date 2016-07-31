from django.contrib import admin
from shop.models import(FishCategory,
                        Seller,
                        Contact,
                        SellerPost,)


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
                    ]

    class Meta:
        model = SellerPost
admin.site.register(SellerPost, SellerPostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'full_name', 'location']

    class Meta:
        model = Contact
admin.site.register(Contact, ContactAdmin)


