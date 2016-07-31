from django.shortcuts import *
from django.contrib.auth.models import User

from shop.forms import (RegisterSellerForm,
                        PostFishCatchForm,
                        UserRegistrationForm,
                        LoginForm,)
from shop.models import Seller, SellerPost, FishCategory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json


def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user = get_object_or_404(User, username=cd['username'])
                    #create sessions
                    request.session['username'] = user.username
                    return HttpResponse(request.session['username'])
                else:
                    return HttpResponse('Your Account is disabled contact admin')
            else:
                return HttpResponse('invalid username/password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'login_form': form, })

def index(request):
    posts = SellerPost.objects.filter(is_available=True)
    return render(request, 'home.html', {'posts': posts, })


response_data = {}


def register_seller(request):
    if request.method == 'POST':

        user_form = UserRegistrationForm(request.POST)
        seller_form = RegisterSellerForm(request.POST)

        if user_form.is_valid() and seller_form.is_valid():
            try:
                new_user = user_form.save(commit=False)
                new_user.set_password(
                    user_form.cleaned_data['password']
                )
                # save the user details
                new_user.save()
                # get the cleaned data from the seller_form
                cd = seller_form.cleaned_data

                phone_no = cd['phone_no']

                location = cd['location']
                # create a new seller object
                seller_obj = Seller.objects.create(
                    seller_username=new_user,
                    phone_no=phone_no,
                    location=location
                )
                seller_obj.save()
                response_data['status'] = 'success'
                response_data['message'] = 'Account Created Successfully'
                return HttpResponse(json.dumps(response_data), content_type='application/json')

            except Exception as e:
                print(str(e))
                response_data['status'] = 'failed'
                response_data['message'] = 'Error Could not create account please try again'
                return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        user_form = UserRegistrationForm()
        seller_form = RegisterSellerForm()

    return render(request, 'register_seller.html', {'user_form': user_form, 'seller_form': seller_form, })


# post the number of fish in the site
def post_my_catch(request):
    if request.method == 'POST':
        fish_catch_form = PostFishCatchForm(request.POST, request.FILES)

        if fish_catch_form.is_valid():
            cd = fish_catch_form.cleaned_data
            username = request.session['username']
            user = get_object_or_404(User, username=username)
            seller = get_object_or_404(Seller, seller_username=user)
            phone_no = seller.phone_no
            fish_category = cd['fish_category']
            quantity = cd['quantity']
            price = cd['price']

            #check if the seller exist in the system
            row_count = (Seller.objects.filter(phone_no=phone_no)).count()
            if row_count == 1:
                # check  if an old post exists
                old_post = (SellerPost.objects.filter(seller=phone_no, fish_category=fish_category)).count()
                if old_post > 0:
                    seller = Seller.objects.get(phone_no=phone_no)
                    old_post1 = SellerPost.objects.get(seller=seller, fish_category=fish_category)
                    old_post1.quantity = quantity
                    old_post1.price = price
                    old_post1.save()
                    return HttpResponse('Post Updated successfully!')
                else:
                    seller_instance = get_object_or_404(Seller, phone_no=phone_no)
                    #seller_name = seller_instance.name
                    fist_category_instance = get_object_or_404(FishCategory, category_name=fish_category)
                    post_instance = SellerPost.objects.create(
                        seller=seller_instance,
                        fish_category=fist_category_instance,
                        quantity=quantity,
                        price=price
                    )
                    post_instance.save()
                    return HttpResponse("Post Created successfully!")
            else:
                return HttpResponseRedirect('/register/')
    else:
        fish_catch_form = PostFishCatchForm()
    return render(request, 'load_catch.html', {'fish_catch_form': fish_catch_form, })
