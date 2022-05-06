from pyexpat import model
from rest_framework import serializers
from .models import User, Community, Comment, Discussion, GriefStage, GriefImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    communities = serializers.HyperlinkedRelatedField(
        view_name='community_detail',
        many=True,
        read_only=True
    )

    username = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'bio', 'image',)


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='artist'
    )

    class Meta:
        model = Community
        fields = ('id', 'user', 'user_id', 'category', 'image', 'grief_stage',)


class DiscussionSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='artist'
    )

    class Meta:
        model = Community
        fields = ('id', 'user', 'user_id', 'category', 'image', 'grief_stage',)
