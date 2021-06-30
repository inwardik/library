from django.urls import path, include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('author', views.AuthorView, basename='Author')

urlpatterns = [
    path("", views.showlist, name="authors_list"),
    path("create", views.CreateAuthor.as_view(), name="create_author"),
    path("delete/<pk>/", views.DeleteAuthor.as_view(), name="delete"),
    path("update/<pk>", views.EditAuthor.as_view(), name="edit"),
    path("author/create/", views.AuthorCreateView.as_view()),
    path("author/detail/<int:pk>/", views.AuthorDetailView.as_view()),
    path("all/", views.AuthorListView.as_view()),
]
