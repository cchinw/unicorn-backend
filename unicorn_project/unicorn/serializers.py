from pyexpat import model
from rest_framework import serializers
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resources, UserProfile


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
