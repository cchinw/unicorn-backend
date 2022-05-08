from django.urls import path
from .views import CommunityCreate, CommunityList, CommunityUpdate, CommunityDetail, CommunityDelete


urlpatterns = [
    # Community Endpoints
    path('api/create/community', CommunityCreate.as_view(), name='create-community'),
    path('api/list/communities', CommunityList.as_view(), name='list-communities'),
    path('api/update/community', CommunityUpdate.as_view(), name='update-community'),
    path('api/detail/community', CommunityDetail.as_view(), name='detail-community'),
    path('api/delete/community', CommunityDelete.as_view(), name='delete-community'),

    # Community Endpoints
    path('api/create/community', CommunityCreate.as_view(), name='create-community'),
    path('api/list/communities', CommunityList.as_view(), name='list-communities'),
    path('api/update/community', CommunityUpdate.as_view(), name='update-community'),
    path('api/detail/community', CommunityDetail.as_view(), name='detail-community'),
    path('api/delete/community', CommunityDelete.as_view(), name='delete-community'),
]
