from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, CommunitySerializer, DiscussionSerializer, CommentSerializer, GriefStageSerializer, GriefImageSerializer
from .models import User, Community, Discussion, Comments, GriefImage, GriefStage


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
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
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class GriefStageList(generics.ListCreateAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefStageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefImageList(generics.ListCreateAPIView):
    queryset = GriefImage.objects.all()
    serializer_class = GriefImageSerializer


class GriefImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GriefImage.objects.all()
    serializer_class = GriefImageSerializer
