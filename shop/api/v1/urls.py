from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^sellers/$', views.SellerList.as_view()),
    url(r'^sellers/(?P<pk>[0-9]+)$', views.SellerDetail.as_view()),
    url(r'^posts/$', views.SellerPostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)$', views.SellerPostDetail.as_view()),
    url(r'^fish/$', views.FishCategoryList.as_view()),
    url(r'^fish/(?P<pk>[0-9]+)$', views.FishCategoryDetail.as_view()),
    url(r'^newsletter/$', views.NewsletterList.as_view()),
    url(r'^newsletter/(?P<pk>[0-9]+)$', views.NewsletterDetail.as_view()),
    url(r'^inbox/$', views.SellerInboxList.as_view()),
    url(r'^inbox/(?P<pk>[0-9]+)$', views.SellerInboxDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

