from django.shortcuts import *
from django.contrib.auth.models import User

from shop.forms import (RegisterSellerForm,
                        PostFishCatchForm,
                        UserRegistrationForm,
                        LoginForm,
                        ContactSellerForm,
                        PostFishCatchEditForm,
)
from shop.models import Seller, SellerPost, FishCategory, SellerInbox
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
import json

from m_fish.settings import API_KEY, USER_NAME


categories = FishCategory.objects.all()


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
                    # create sessions
                    request.session['username'] = user.username
                    request.session.modified = True
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Your Account is disabled contact admin')
            else:
                message = "invalid username/password "
                form = LoginForm()
            return render(request, 'login.html', {'message': message, 'login_form': form, })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'login_form': form, })


def logout_user(request):
    logout(request)
    try:
        del request.session['username']
        request.session.modified = True
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


def index(request):
    categories = FishCategory.objects.all()
    posts = SellerPost.objects.filter(is_available=True)

    return render(request, 'home.html',
                  {'categories': categories,
                   'posts': posts, })

response_data = {}


#@transaction.atomic
def register_seller(request):
    if request.method == 'POST':

        user_form = UserRegistrationForm(request.POST)
        seller_form = RegisterSellerForm(request.POST)
        print('am here')
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
                    user=new_user,
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

    return render(request, 'register_seller.html', {'user_form': user_form,
                                                    'seller_form': seller_form,
                                                    'categories': categories,
    })


# post the number of fish in the site
def post_my_catch(request):
    if request.method == 'POST':
        fish_catch_form = PostFishCatchForm(request.POST, request.FILES)

        if fish_catch_form.is_valid():
            cd = fish_catch_form.cleaned_data
            username = request.session.get('username', '')
            user = get_object_or_404(User, username=username)
            seller = get_object_or_404(Seller, user=user)
            phone_no = seller.phone_no
            fish_category = cd['fish_category']
            quantity = cd['quantity']
            price = cd['price']
            photo = cd['fish_photo']

            seller_instance = get_object_or_404(Seller, phone_no=phone_no)
            fist_category_instance = get_object_or_404(FishCategory, category_name=fish_category)
            post_instance = SellerPost.objects.create(
                seller=seller_instance,
                fish_category=fist_category_instance,
                fish_photo=photo,
                quantity=quantity,
                price=price
            )
            post_instance.save()
            return HttpResponseRedirect("/")

    else:
        fish_catch_form = PostFishCatchForm()
    return render(request, 'load_catch.html', {'fish_catch_form': fish_catch_form,
                                               'categories': categories, })


# working now.
def edit_post(request, pk):
    post = SellerPost.objects.get(pk=pk)
    fish_cat = post.fish_category
    qty = post.quantity
    price = post.price
    form_args = {'fish_category': fish_cat, 'quantity': qty, 'price': price, }

    if request.method == 'POST':
        form = PostFishCatchForm(request.POST, request.FILES, initial=form_args)
        if form.is_valid():
            cd = form.cleaned_data
            fish_category = str(cd['fish_category'])
            quantity = float(cd['quantity'])
            price = float(cd['price'])
            photo = cd['fish_photo']
            category_instance = get_object_or_404(FishCategory, category_name=fish_category)
            post.fish_category = category_instance
            post.quantity = quantity
            post.price = price
            post.fish_photo = photo
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostFishCatchEditForm(initial=form_args)
    return render(request, 'edit_post.html', {'form': form, 'categories': categories, })


def contact_seller(request, pk=None):
    post = get_object_or_404(SellerPost, pk=pk)
    if request.method == "POST":
        form = ContactSellerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone_no = cd['phone_no']
            amount = float(cd['amount'])
            price = float(post.price)
            total_price = amount * price
            seller_phone = post.seller.phone_no
            fish_category = str(post.fish_category)
            seller = post.seller.user

            # compose the message the seller will get

            message = "Dear {0} m-fish is glad to inform you that {1}" \
                      " wishes to purchase {2} Kgs of {3}.\n " \
                      "The sale price will be {4} Ksh.\n" \
                      " please contact this customer to make the sale" \
                      "".format(seller, phone_no, amount, fish_category, total_price)
            # create Model instance of  SellerInbox model
            inbox_msg = SellerInbox.objects.create(
                seller_phone=seller_phone,
                customer_phone=phone_no,
                fish_category=fish_category,
                price_per_kg=price,
                amount_requested=amount,
                message_sent=message
            )
            inbox_msg.save()
            post.seller.times_contacted += 1
            post.save()
            return HttpResponse(message)

    else:
        form = ContactSellerForm()
    return render(request, 'contact_seller.html', {'form': form, 'categories': categories, })


def post_list(request, category_slug=None):
    category = None
    posts = SellerPost.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(FishCategory, slug=category_slug)
        posts = posts.filter(fish_category=category)

    return render(request, 'post_list.html',
                  {'category': category,
                   'categories': categories,
                   'posts': posts, })


def post_detail(request, pk):
    post = SellerPost.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post, 'categories': categories, })

