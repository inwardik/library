from django.urls import path
from .views import create_user, users_list, delete_user, edit_user, redirect, CustomUserList, CustomUserCreate, CustomUserDetail
from rest_framework import routers

urlpatterns = [
    path('', users_list, name='users_list'),
    path('create/', create_user, name='create_user'),
    path('delete/<int:user_id>', delete_user),
    path('edit/<int:user_id>', edit_user),
    # path("user/create/", CustomUserCreate.as_view()),
    # path("user/detail/<int:pk>/", CustomUserDetail.as_view()),
    # path("all/", CustomUserList.as_view()),
]
