from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'middle_name', 'last_name', 'updated_at',
                  'created_at', 'role', 'is_active']
