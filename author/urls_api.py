from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.AuthorCreateView.as_view()),
    path("detail/<int:pk>/", views.AuthorDetailView.as_view()),
    path("all/", views.AuthorListView.as_view()),
]
