from django.urls import path
from .views import ResendEmailConfirmation, VerifyEmailView, UserLoginView, ChangePasswordSerializer, DeactivateUserView, ActivateUserView, UnicornSignUpView, UserList, UserDetail, UserUpdate, CommunityCreate, CommunityList, CommunityUpdate, CommunityDetail, CommunityDelete, GriefStageUpdate, GriefStageList, GriefStageDetail, DiscussionCreate, DiscussionUpdate, DiscussionList, DiscussionDetail, DiscussionDelete, CommentCreate, CommentUpdate, CommentList, CommentDetail, CommentDelete, ResourceList, ResourceDetail, ResourceCreate, DirectMesageCreate, DirectMesageUpdate, DirectMesageList, DirectMesageDetail, DirectMesageDelete


urlpatterns = [
    # User Endpoints
    path('api/register/user', UnicornSignUpView.as_view(),
         name='register-unicorn-user'),
    path('api/login/user', UserLoginView.as_view(), name='login-unicorn-user'),
    path('api/auth/session', UserLoginView.as_view(), name='check-session'),
    path('api/detail/unicorn-user/<pk>', UserDetail.as_view(), name='view-user'),
    path('api/update/unicorn-user/<pk>',
         UserUpdate.as_view(), name='update-user'),
    path('api/list/users', UserList.as_view(),
         name='list-unicorn-users'),

    # Grief Stage Endpoints
    path('api/list/grief-stages', GriefStageList.as_view(),
         name='list-grief-stages'),
    path('api/update/grief-stage/<pk>', GriefStageUpdate.as_view(),
         name='update-grief-stage'),
    path('api/detail/grief-stage/<pk>', GriefStageDetail.as_view(),
         name='detail-grief-stage'),

    # Community Endpoints
    path('api/list/community/<int:members>',
         CommunityList.as_view(), name='get-community-members'),
    path('api/detail/community/<int:creator>',
         CommunityDetail.as_view(), name='get-community-creator'),
    path('api/create/community', CommunityCreate.as_view(), name='create-community'),
    path('api/detail/community/<int:grief_stage>',
         CommunityDetail.as_view(), name='get-community-by-grief-stage'),
    path('api/update/community/<pk>',
         CommunityUpdate.as_view(), name='update-community'),
    path('api/update/community/<int:members>',
         CommunityUpdate.as_view(), name='join-community'),
    path('api/detail/community/<pk>',
         CommunityDetail.as_view(), name='detail-community'),
    path('api/delete/community/<pk>',
         CommunityDelete.as_view(), name='delete-community'),

    # Discussion Endpoints
    path('api/create/discussion', DiscussionCreate.as_view(),
         name='create-discussion'),
    path('api/list/discussions', DiscussionList.as_view(), name='list-discussions'),
    path('api/list/discussions/<int:community>',
         DiscussionList.as_view(), name='list-discussions-by-community'),
    path('api/list/discussions/<int:user>',
         DiscussionList.as_view(), name='list-discussions-by-users'),
    path('api/update/discussion/<pk>', DiscussionUpdate.as_view(),
         name='update-discussion'),
    path('api/detail/discussion/<pk>', DiscussionDetail.as_view(),
         name='detail-discussion'),
    path('api/delete/discussion/<pk>', DiscussionDelete.as_view(),
         name='delete-discussion'),

    # Comments Endpoints
    path('api/create/comment', CommentCreate.as_view(), name='create-comment'),
    path('api/list/comments', CommentList.as_view(), name='list-comments'),
    path('api/list/comments/<int:discussion>',
         CommentList.as_view(), name='list-comments-by-discussion'),
    path('api/update/comment/<pk>', CommentUpdate.as_view(), name='update-comment'),
    path('api/detail/comment/<pk>', CommentDetail.as_view(), name='detail-comment'),
    path('api/delete/comment/<pk>', CommentDelete.as_view(), name='delete-comment'),

    # Resources Endpoints
    path('api/create/resource', ResourceCreate.as_view(), name='create-resource'),
    path('api/list/resources', ResourceList.as_view(), name='list-resources'),
    path('api/detail/resource/<pk>',
         ResourceDetail.as_view(), name='detail-resource'),

    # Direct Message Endpoints
    path('api/create/direct-message', DirectMesageCreate.as_view(),
         name='create-direct-message'),
    path('api/list/direct-messages', DirectMesageList.as_view(),
         name='list-direct-messages'),
    path('api/update/direct-message/<pk>', DirectMesageUpdate.as_view(),
         name='update-direct-message'),
    path('api/detail/direct-message/<pk>', DirectMesageDetail.as_view(),
         name='detail-direct-message'),
    path('api/delete/direct-message/<pk>', DirectMesageDelete.as_view(),
         name='delete-direct-message'),
]
