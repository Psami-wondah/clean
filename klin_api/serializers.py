from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import User
from main_app.models import Profile
from django.db import transaction
from rest_framework.validators import UniqueValidator


class UserSerializer(UserCreateSerializer):
    is_giver = serializers.BooleanField(default=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'location',
                  'password', 'is_giver', 'is_collector']


class AgencySerializer(UserCreateSerializer):
    is_collector = serializers.BooleanField(default=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'password', 'is_collector', 'is_giver'
                  ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'image', 'section_points']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileUpdateSerializer()
    class Meta:
        model = User
        fields = ['profile', 'username', 'first_name', 'last_name', 'phone', 'location']

    def update(self, instance, validated_data):
        tracks_data = validated_data.pop('profile')
        profile = instance.profile
        instance.save()
        profile.image = tracks_data.get(
            'image',
            profile.image
        )
        profile.save()
        return instance








