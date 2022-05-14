from builtins import super

from allauth.account.signals import email_confirmed
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, APIView
from rest_framework.exceptions import APIException
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC, EmailAddress
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_auth.registration.serializers import VerifyEmailSerializer
from rest_framework import generics
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView, UpdateAPIView, get_object_or_404)


# Create your views here.
from .serializers import UserSerializer, UserProfileSerializer, ResendEmailSerializer, ChangePasswordSerializer, UnicornLoginSerializer, UnicornUserActivateSerializer, UnicornUserDeactivateSerializer, UnicornRegisterSerializer, GriefStageSerializer, CommunitySerializer, DiscussionSerializer, CommentSerializer, DirectMessageSerializer, ResourceSerializer
from .models import UnicornUser, UserProfile, Community, Comment, Discussion, GriefStage, DirectMessage, Resources


def index(request):
    return HttpResponse("Welcome to Unicorn API Page")

# User Views


@api_view()
def django_rest_auth_null():
    return Response(status=status.HTTP_400_BAD_REQUEST)


# User Management View


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = email_address.user
    user.email_verified = True

    user.save()

# request a new confirmation email


User = get_user_model()


# request a new confirmation email
class ResendEmailConfirmation(APIView):
    permission_classes = [AllowAny]
    serializer_class = ResendEmailSerializer

    def post(self, request):

        try:
            user = User.objects.get(email=request.data['email'])
            emailAddress = EmailAddress.objects.filter(
                user=user, verified=True).exists()

            if emailAddress:
                return Response({'message': 'This email has already been  verified'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                send_email_confirmation(request, user=user)
                return Response({'message': 'Verification email resent'}, status=status.HTTP_201_CREATED)
        except APIException:
            return Response({'message': 'This email does not exist, please create a new account'},
                            status=status.HTTP_403_FORBIDDEN)


class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        try:
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            return Response({'detail': _('Successfully confirmed email.')}, status=status.HTTP_200_OK)
        except EmailConfirmation.DoesNotExist:
            return Response({'detail': _('Error Incorrect key.')}, status=status.HTTP_404_NOT_FOUND)

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                raise EmailConfirmation.DoesNotExist
        return emailconfirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs


class UserLoginView(LoginView):

    def get_response(self):
        response = super().get_response()
        data = {"message": "Welcome back, {} {}".format(self.user.first_name, self.user.last_name, ),
                "code": response.status_code,
                "user_type": self.user.user_type, "user_id": self.user.id}
        response.data.update(data)

        return response


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    serializer_class = ChangePasswordSerializer
    model = UnicornUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
            }

# Deactivate User Account


class DeactivateUserView(RetrieveUpdateAPIView):
    """
    An endpoint for deactivating a user.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = UnicornUserDeactivateSerializer
    queryset = UnicornUser.objects.all()

    def update(self, request, *args, **kwargs):
        email = request.data.get("email")
        user = UnicornUser.objects.get(email=email)
        user.is_active = False
        user.save()
        response = {"email": email, "message": "User successfully disabled."}
        response = Response(response)
        return response


class ActivateUserView(RetrieveUpdateAPIView):
    """
    An endpoint for activating a user.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = UnicornUserActivateSerializer
    queryset = UnicornUser.objects.all()

    def update(self, request, *args, **kwargs):
        # response = super().update(request, *args, **kwargs)
        email = request.data.get("email")
        user = UnicornUser.objects.get(email=email)
        user.is_active = True
        user.save()
        response = {"email": email, "message": "User successfully activated."}
        response = Response(response)
        return response


class UnicornSignUpView(RegisterView):
    serializer_class = UnicornRegisterSerializer
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def create(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username', None),
            'email': request.data.get('email', None),
            'password1': request.data.get('password1', None),
            'password2': request.data.get('password2', None),
            'bio': request.data.get('bio', None),
            'avatar': request.data.get('avatar', None),
        }

        serializer = UnicornRegisterSerializer(data=data)
        if serializer.is_valid():
            user = self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            body = self.get_response_data(user)
            token, created = Token.objects.get_or_create(user=user.id)
            body["token"] = token.key
            body["email"] = user.email
            body["id"] = user.id
            response = Response(body,
                                status=status.HTTP_201_CREATED,
                                headers=headers)
            return response

        else:
            response = Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            return response


class UserList(generics.ListCreateAPIView):
    queryset = UnicornUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnicornUser.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = UnicornUser.objects.all()
    serializer_class = UserSerializer
# Grief Stage Views


class GriefStageUpdate(generics.RetrieveUpdateAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefStageList(generics.ListAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefStageDetail(generics.RetrieveAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


# Community Views
class CommunityCreate(generics.CreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityUpdate(generics.RetrieveUpdateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityList(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityDetail(generics.RetrieveAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityDelete(generics.DestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


# Discussion Views
class DiscussionCreate(generics.CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DiscussionUpdate(generics.RetrieveUpdateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DiscussionList(generics.ListAPIView):
    queryset = Discussion.objects.all()
    lookup_field = 'community'
    serializer_class = DiscussionSerializer

    def get_queryset(self, **kwargs):
        try:
            community = kwargs['community']
            discussions = Discussion.objects.filter(community=community)
            return discussions
        except Discussion.DoesNotExist():
            return {}


class DiscussionDetail(generics.RetrieveAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DiscussionDelete(generics.DestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


# Comment Views

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Resource Views
class ResourceCreate(generics.CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


class ResourceList(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetail(generics.RetrieveAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


# Direct Message Views

class DirectMesageCreate(generics.CreateAPIView):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer


class DirectMesageUpdate(generics.RetrieveUpdateAPIView):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer


class DirectMesageList(generics.ListAPIView):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer


class DirectMesageDetail(generics.RetrieveAPIView):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer


class DirectMesageDelete(generics.DestroyAPIView):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer
