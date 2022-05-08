from pyexpat import model
from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resources, UserProfile
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnicornUser
        fields = '__all__'


class GriefStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GriefStage
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
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


class UnicornLoginSerializer(LoginSerializer):
    username = None


class ChangePasswordSerializer(serializers.Serializer):
    model = UnicornUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.CharField()
