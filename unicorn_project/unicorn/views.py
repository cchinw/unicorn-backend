from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, UserProfileSerializer, GriefStageSerializer, CommunitySerializer, DiscussionSerializer, CommentSerializer, DirectMessageSerializer, ResourceSerializer
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resources, UserProfile


# class UserList(generics.ListCreateAPIView):
#     queryset = UnicornUser.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UnicornUser.objects.all()
#     serializer_class = UserSerializer
def index(request):
    return HttpResponse("Welcome to Unicorn API Page")


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
