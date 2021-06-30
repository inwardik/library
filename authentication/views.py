from django.shortcuts import render, redirect
from .models import CustomUser
from rest_framework import generics
from . import serializers


def create_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        CustomUser.create(email, password, first_name, middle_name, last_name)
        return redirect('users_list')
    return render(request, 'authentication/create_user.html')


def users_list(request):
    users = CustomUser.get_all()
    return render(request, 'authentication/users_list.html', {'users': users})


def delete_user(request, user_id):
    CustomUser.delete_by_id(user_id)
    return redirect('users_list')


def edit_user(request, user_id):
    user = CustomUser.get_by_id(user_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')
        is_active = request.POST.get('is_active')
        password = request.POST.get('password')
        user.update(first_name, last_name, middle_name, password, role, is_active)
        return redirect('users_list')
    else:
        return render(request, 'authentication/edit_user.html', {'user': user})


def redirect_to_book(request):
    return redirect('book/')


class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class CustomUserCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
