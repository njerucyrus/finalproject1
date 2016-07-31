from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_seller, name='register'),
    url(r'^post/$', views.post_my_catch, name='post'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^post/contact/(?P<pk>\d+)/$', views.contact_seller, name='contact_seller'),

]