from django import forms
from shop.models import Seller, SellerPost
from django.contrib.auth.models import User



FISH_CATEGORY = (
    ('Tilapia', 'Tilapia'),
    ('Nile Perch', 'Nile Perch'),
    ('Dagaa', 'Dagaa'),
    ('Shrawl', 'Shrawl'),
    ('Cat Fish', 'Cat Fish'),)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class RegisterSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('phone_no', 'location',)


class PostFishCatchForm(forms.ModelForm):
    class Meta:
        model = SellerPost
        fields = ('fish_category', 'price', 'quantity', )
