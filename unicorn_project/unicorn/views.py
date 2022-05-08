from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, UserProfileSerializer, GriefStageSerializer, CommunitySerializer, DiscussionSerializer, CommentSerializer, DirectMessageSerializer, ResourceSerializer
from .models import UnicornUser, UserProfile, Community, Comment, Discussion, GriefStage, DirectMessage, Resources


# class UserList(generics.ListCreateAPIView):
#     queryset = UnicornUser.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UnicornUser.objects.all()
#     serializer_class = UserSerializer
def index(request):
    return HttpResponse("Welcome to Unicorn API Page")

# Grief Stage Views
# class GriefStageCreate(generics.CreateAPIView):
#     queryset = GriefStage.objects.all()
#     serializer_class = GriefStageSerializer


class GriefStageUpdate(generics.RetrieveUpdateAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefStageList(generics.ListAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


class GriefStageDetail(generics.RetrieveAPIView):
    queryset = GriefStage.objects.all()
    serializer_class = GriefStageSerializer


# class GriefStageDelete(generics.DestroyAPIView):
#     queryset = GriefStage.objects.all()
#     serializer_class = GriefStageSerializer

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
    serializer_class = DiscussionSerializer


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

# class ResourceCreate(generics.CreateAPIView):
#     queryset = Resources.objects.all()
#     serializer_class = ResourceSerializer


# class ResourceUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Resources.objects.all()
#     serializer_class = ResourceSerializer


class ResourceList(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetail(generics.RetrieveAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


# class ResourceDelete(generics.DestroyAPIView):
#     queryset = Resources.objects.all()
#     serializer_class = ResourceSerializer


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
