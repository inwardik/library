from django.urls import path
from .views import CreateBook, EditBook, DeleteBook, read

urlpatterns = [
    path("", read, name="books_list"),
    path("create", CreateBook.as_view(), name="create_book"),
    path("delete/<pk>/", DeleteBook.as_view(), name="delete"),
    path("edit/<pk>/", EditBook.as_view(), name="edit")

]