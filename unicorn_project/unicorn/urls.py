from django.urls import path
from .views import CommunityCreate, CommunityList, CommunityUpdate, CommunityDetail, CommunityDelete, GriefStageUpdate, GriefStageList, GriefStageDetail, DiscussionCreate, DiscussionUpdate, DiscussionList, DiscussionDetail, DiscussionDelete, CommentCreate, CommentUpdate, CommentList, CommentDetail, CommentDelete, ResourceList, ResourceDetail, DirectMesageCreate, DirectMesageUpdate, DirectMesageList, DirectMesageDetail, DirectMesageDelete


urlpatterns = [
    # Grief Stage Endpoints
    path('api/list/grief-stages', GriefStageList.as_view(),
         name='list-grief-stages'),
    path('api/update/grief-stage', GriefStageUpdate.as_view(),
         name='update-grief-stage'),
    path('api/detail/grief-stage', GriefStageDetail.as_view(),
         name='detail-grief-stage'),

    # Community Endpoints
    path('api/create/community', CommunityCreate.as_view(), name='create-community'),
    path('api/list/communities', CommunityList.as_view(), name='list-communities'),
    path('api/update/community', CommunityUpdate.as_view(), name='update-community'),
    path('api/detail/community', CommunityDetail.as_view(), name='detail-community'),
    path('api/delete/community', CommunityDelete.as_view(), name='delete-community'),

    # Discussion Endpoints
    path('api/create/discussion', DiscussionCreate.as_view(),
         name='create-discussion'),
    path('api/list/discussions', DiscussionList.as_view(), name='list-discussions'),
    path('api/update/discussion', DiscussionUpdate.as_view(),
         name='update-discussion'),
    path('api/detail/discussion', DiscussionDetail.as_view(),
         name='detail-discussion'),
    path('api/delete/discussion', DiscussionDelete.as_view(),
         name='delete-discussion'),

    # Discussion Endpoints
    path('api/create/comment', CommentCreate.as_view(), name='create-comment'),
    path('api/list/comments', CommentList.as_view(), name='list-comments'),
    path('api/update/comment', CommentUpdate.as_view(), name='update-comment'),
    path('api/detail/comment', CommentDetail.as_view(), name='detail-comment'),
    path('api/delete/comment', CommentDelete.as_view(), name='delete-comment'),

    # Resources Endpoints
    path('api/list/resources', ResourceList.as_view(), name='list-resources'),
    path('api/detail/resource', ResourceDetail.as_view(), name='detail-resource'),

    # Direct Message Endpoints
    path('api/create/direct-message', DirectMesageCreate.as_view(),
         name='create-direct-message'),
    path('api/list/direct-messages', DirectMesageList.as_view(),
         name='list-direct-messages'),
    path('api/update/direct-message', DirectMesageUpdate.as_view(),
         name='update-direct-message'),
    path('api/detail/direct-message', DirectMesageDetail.as_view(),
         name='detail-direct-message'),
    path('api/delete/direct-message', DirectMesageDelete.as_view(),
         name='delete-direct-message'),
]
