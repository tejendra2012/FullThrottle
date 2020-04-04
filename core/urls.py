from django.urls import include, path
from .views import getUsersViews , getUserInfoViews

urlpatterns = [
    path('users/', getUsersViews,name='all_users'), # new
    path('users/<str:user_id>/', getUserInfoViews , name='user_info'),
]