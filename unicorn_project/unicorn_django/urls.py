"""unicorn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ast import Index
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from unicorn.views import index
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_auth.views import PasswordResetConfirmView

from unicorn.views import index, UserLoginView, UnicornSignUpView, \
    VerifyEmailView, ChangePasswordView, ResendEmailConfirmation, DeactivateUserView, ActivateUserView

schema_view = get_schema_view(
    openapi.Info(
        title="Unicorn Services API",
        default_version='v1',
        description="Unicorn API",
    ),
)
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('unicorn/', include('unicorn.urls')),
    path('swagger-docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    # Registration and Authentication
    path('rest-auth/password/reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('rest-auth/password/reset/confirm/<str:uidb64>/', PasswordResetConfirmView,
         name='password_reset_confirm'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/unicorn/registration/', UnicornSignUpView.as_view()),
    path('rest-auth/accounts/login/',
         UserLoginView.as_view(), name='custom-login'),
    path('rest-auth/resend-confirmation-email/',
         ResendEmailConfirmation.as_view(), name='resend-email-confirmation'),
    path('rest-auth/deactivate-user/', DeactivateUserView.as_view()),
    path('rest-auth/activate-user/', ActivateUserView.as_view()),
    path('rest-auth/change-password/',
         ChangePasswordView.as_view(), name='change-password'),
    path('rest-auth/account-confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    path('rest-auth/account-confirm-email/<str:key>/', VerifyEmailView.as_view(),
         name='account_confirm_email'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
