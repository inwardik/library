from django.urls import path, include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('author', views.AuthorView, basename='Author')

urlpatterns = [
    path("create/", views.CustomUserCreate.as_view()),
    path("detail/<int:pk>/", views.CustomUserDetail.as_view()),
    path("all/", views.CustomUserList.as_view()),
]