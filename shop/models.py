from django.db import models
from django.contrib.auth.models import User

# Create your models here.

FISH_CATEGORY = (
        ('Tilapia', 'Tilapia'),
        ('Nile Perch', 'Nile Perch'),
        ('Dagaa', 'Dagaa'),
        ('Shrawl', 'Shrawl'),
        ('Cat Fish', 'Cat Fish'),

    )


class FishCategory(models.Model):
    category_name = models.CharField(max_length=20, choices=FISH_CATEGORY, default=FISH_CATEGORY[0][0], unique=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)

    class Meta:
        verbose_name_plural = 'Fish'

    def __str__(self):
        return self.category_name

# represent fisherman


class Seller(models.Model):
    seller_username = models.OneToOneField(User)
    phone_no = models.CharField(max_length=13, primary_key=True)
    location = models.CharField(max_length=100, blank=True, default='Kisumu')

    class Meta:
        verbose_name_plural = 'Sellers'

    def __str__(self):  # should be __unicode__(self): in python 2.x.x
        return self.phone_no


# model to hold the data  of items a seller has
class SellerPost(models.Model):
    seller = models.ForeignKey(Seller)
    fish_category = models.ForeignKey(FishCategory, related_name='fish')
    fish_photo = models.ImageField(upload_to='assets/img', blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    price = models.DecimalField("Price per Kg", max_digits=10, decimal_places=2, default=0000.00, null=True)
    available_amt = models.DecimalField(max_digits=10, decimal_places=2, default=0000.00, null=True)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'post for '.format(self.seller.phone_no)


class Contact(models.Model):
    phone_number = models.CharField(max_length=13)
    full_name = models.CharField(max_length=100, blank=True, default='Seller')
    location = models.CharField(max_length=100, blank=True, default='Kisumu')

    def __str__(self):
        return self.phone_number
