from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_seller, name='register'),
    url(r'^create-post/$', views.post_my_catch, name='post'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^post/contact/(?P<pk>\d+)/$', views.contact_seller, name='contact_seller'),
    url(r'^posts/(?P<category_slug>[-\w]+)/$', views.post_list, name='post_list_by_category'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^newsletter/$', views.newsletter_signup, name='newsletter'),
    url(r'^support/$', views.contact_us, name='contact_us'),

]
