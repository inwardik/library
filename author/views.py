from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from rest_framework import viewsets, generics
from .models import Author
from .forms import AuthorForm
from .serializers import AuthorListSerializer, AuthorDetailSerializer


def showlist(request):
    authors_list = Author.objects.all()
    return render(request, "author/read.html", {"authors": authors_list})


class CreateAuthor(ListView):
    template_name = 'author/create.html'
    model = Author

    def get(self, request):
        form = AuthorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
        return render(request, self.template_name, {'form': form})


class EditAuthor(UpdateView):
    template_name = 'author/update.html'
    model = Author
    fields = ['name', 'surname', 'patronymic']
    success_url = reverse_lazy('authors_list')


class DeleteAuthor(ListView):
    template_name = 'author/delete_author.html'
    model = Author

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})

    def post(self, request, pk):
        Author.delete_by_id(pk)
        return redirect('authors_list')


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()