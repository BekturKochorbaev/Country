from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user_comments/', UserCommentsHistoryAPIView.as_view(), name='user_comments'),

    path('password_reset/verify_code/', verify_reset_code, name='verify_reset_code'),
    path('password_reset/', custom_password_reset, name='custom_password_reset'),
]