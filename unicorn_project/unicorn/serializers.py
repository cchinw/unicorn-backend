from pyexpat import model
from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resources, UserProfile
from django.utils.translation import gettext as _
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from rest_auth.serializers import LoginSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnicornUser
        fields = '__all__'


class GriefStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GriefStage
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    """

       User Account

    """

    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'


class UnicornUserDeactivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnicornUser
        fields = ['email']


class UnicornUserActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnicornUser
        fields = ['email']


class UnicornRegisterSerializer(serializers.Serializer):
    avatar = serializers.ImageField(required=False)
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    bio = serializers.CharField(required=False, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        profile = UserProfile.objects.create(user=user)
        profile.avatar = self.cleaned_data.get('avatar')
        profile.user.user_type = 2
        profile.save()
        user.save()
        return user


class UnicornLoginSerializer(LoginSerializer):
    username = ['username']


class ChangePasswordSerializer(serializers.Serializer):
    model = UnicornUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.CharField()
