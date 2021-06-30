from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from rest_framework import generics
from .serializers import BookListSerializer, BookDetailSerializer

from .models import Book
from .forms import BookForm


def read(request):
    books_list = Book.objects.all()
    # book.save()
    return render(request, 'book/read.html', {"books": books_list})


class CreateBook(ListView):
    template_name = 'book/create.html'
    model = Book

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
        return render(request, self.template_name, {'form': form})


class EditBook(UpdateView):
    template_name = 'book/update.html'
    model = Book
    fields = ['name', 'description', 'count', 'authors']
    success_url = reverse_lazy('books_list')


class DeleteBook(ListView):
    template_name = 'book/delete_book.html'
    model = Book

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})

    def post(self, request, pk):
        Book.delete_by_id(pk)
        return redirect('books_list')

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class BookListView(generics.ListAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

