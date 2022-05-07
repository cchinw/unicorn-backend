from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, UserProfileSerializer, GriefStageSerializer, CommunitySerializer, DiscussionSerializer, CommentSerializer, DirectMessageSerializer, ResourceSerializer
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resources, UserProfile


class UserList(generics.ListCreateAPIView):
    queryset = UnicornUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnicornUser.objects.all()
    serializer_class = UserSerializer


class CommunityList(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class DiscussionList(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GriefStageList(generics.ListCreateAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefStageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer
