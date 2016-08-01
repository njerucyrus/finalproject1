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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=13, unique=True)
    location = models.CharField(max_length=100, blank=True, default='')
    times_contacted = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Sellers'

    def __str__(self):  # should be __unicode__(self): in python 2.x.x
        return self.phone_no


# model to hold the data  of items a seller has
class SellerPost(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    fish_category = models.ForeignKey(FishCategory, related_name='fish', on_delete=models.CASCADE)
    fish_photo = models.ImageField(upload_to='assets/img', blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    price = models.DecimalField("Price per Kg", max_digits=10, decimal_places=2, default=0000.00, null=True)
    available_amt = models.DecimalField(max_digits=10, decimal_places=2, default=0000.00, null=True)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = SellerPost.objects.get(id=self.id)
            if this.fish_photo != self.fish_photo:
                this.fish_photo.delete(save=False)
        except Exception as e:
            pass  # when new photo then we do nothing, normal case
        super(SellerPost, self).save(*args, **kwargs)


class Meta:
    ordering = ('-date_posted', )


def __str__(self):
    return 'post for '.format(self.seller.phone_no)


class SellerInbox(models.Model):
    customer_phone = models.CharField(max_length=13)
    seller_phone = models.CharField(max_length=13)
    fish_category = models.CharField(max_length=50)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    message_sent = models.TextField(max_length=200)
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_sent',)
        verbose_name_plural = "Contact Messages Sent"

    def __str__(self):
        return self.seller_phone


class Newsletter(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Newsletter"

    def __str__(self):
        return self.email

