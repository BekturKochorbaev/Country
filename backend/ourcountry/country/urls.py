from django.urls import path, include
from .views import *
from rest_framework import routers


# FOR CHARLES DEO
router = routers.DefaultRouter()
# router.register(r'hotel_review', HotelsReviewViewSet, basename='hotel_review')

urlpatterns = [
    path('', include(router.urls)),

    path('user_profile_create/', UserProfileCreateAPIView.as_view(), name='user_profile_create'),

    path('home/', HomeListAPIView.as_view(), name='home'),
    path('region/', RegionListAPIView.as_view(), name='region'),

    path('attractions/', AttractionsListAPIView.as_view(), name='attractions'),
    path('attractions/<int:pk>/', AttractionsDetailAPIView.as_view(), name='attractions_detail'),
    path('attraction_review_list/', AttractionReviewListAPIView.as_view(), name='attraction_review_list'),
    path('attraction_review_create/', AttractionReviewCreateAPIView.as_view(), name='attraction_review_create'),

    path('popular_places/', PopularPlacesListAPI.as_view(), name='region_popular_places'),
    path('popular_places/<int:pk>/', PopularPlacesDetailAPI.as_view(), name='region_popular_places_detail'),
    path('popular_places_review/', PopularReviewListAPIView.as_view(), name='popular_places_review'),
    path('popular_places_review_create/', PopularReviewCreateAPIView.as_view(), name='popular_places_review_create'),

    path('hotels/', HotelsListAPIView.as_view(), name='hotels_list'),
    path('hotels/<int:pk>/', HotelsDetailAPIView.as_view(), name='hotel_detail'),
    path('hotels_review_list/', HotelsReviewListAPIView.as_view(), name='hotels_review_list'),
    path('hotels_review_create/', HotelReviewCreateAPiView.as_view(), name='hotels_review_create'),

    path('kitchen/', KitchenListView.as_view(), name='kitchen_list'),
    path('kitchen/<int:pk>/', KitchenDetailView.as_view(), name='kitchen_detail'),
    path('kitchen_review_create/', KitchenReviewCreateAPIView.as_view(), name='kitchen_review_create'),
    path('kitchen_review_list/', KitchenReviewListAPIView.as_view(), name='kitchen_review_list'),

    path('event/', EventListAPiView.as_view(), name='event'),

    path('culture_list/', CultureListAPiView.as_view(), name='culture_list'),

    path('games/', GamesViewSet.as_view({'get': "list"}), name='games_list'),

    path('culture_kitchen/', CultureKitchenViewSet.as_view({'get': "list"}), name='culture_kitchen'),

    path('national_clothes/', NationalClothesViewSet.as_view({'get': "list"}), name='national_clothes_list'),

    path('currency/', CurrencyViewSet.as_view({'get': "list"}), name='currency_list'),

    path('handcrafts/', HandCraftsViewSet.as_view({'get': "list"}), name='handcrafts_list'),

    path('instruments/', NationalInstrumentsViewSet.as_view({'get': "list"}), name='instruments_list'),

    path('gallery/', GalleryListAPIView.as_view(), name='gallery'),
    path('gallery_review_create/', GalleryReviewCreateAPIView.as_view(), name='gallery_review_create'),

    path('favorite/', FavoriteItemViewSet.as_view({'get': 'list'}), name='favorite'),

    path('favorite_item/', FavoriteItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_item_list'),
    path('favorite_item/<int:pk>/', FavoriteItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='favorite_item_detail'),


]