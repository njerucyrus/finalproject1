from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import(
    SellerSerializer,
    SellerInboxSerializer,
    SellerPostSerializer,
    FishCategorySerializer,
    NewsletterSerializer,
)
from shop.models import(
    Seller,
    SellerPost,
    SellerInbox,
    FishCategory,
    Newsletter,
)


class SellerList(ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerPostList(ListCreateAPIView):
    queryset = SellerPost.objects.all()
    serializer_class = SellerPostSerializer


class SellerPostDetail(RetrieveUpdateDestroyAPIView):
    queryset = SellerPost.objects.all()
    serializer_class = SellerPostSerializer


class FishCategoryList(ListCreateAPIView):
    queryset = FishCategory.objects.all()
    serializer_class = FishCategorySerializer


class FishCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = FishCategory.objects.all()
    serializer_class = FishCategorySerializer


class NewsletterList(ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class NewsletterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class SellerInboxList(ListCreateAPIView):
    queryset = SellerInbox.objects.all()
    serializer_class = SellerInboxSerializer


class SellerInboxDetail(RetrieveUpdateDestroyAPIView):
    queryset = SellerInbox.objects.all()
    serializer_class = SellerInboxSerializer
