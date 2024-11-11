from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from .views import UserView
from transaction.views import ProductView , TransactionView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'), # login url
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # url for refresh token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # url for verifying access token
    path('api/auth/users/' , UserView.as_view()), # url for register (post)  , get all user (get) , change password (patch)
    path('api/products/' , ProductView.as_view()), #ignore this for now
    path('api/transactions/' , TransactionView.as_view()), # ignore this
]
