from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    #url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_seller, name='register'),
    url(r'^post/$', views.post_my_catch, name='post'),

]