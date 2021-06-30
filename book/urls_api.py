from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.BookCreateView.as_view()),
    path("detail/<int:pk>/", views.BookDetailView.as_view()),
    path("all/", views.BookListView.as_view()),
]
