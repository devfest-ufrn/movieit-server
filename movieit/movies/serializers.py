from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieTheatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTheather
        fields = '__all__'

class NowPlayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowPlaying
        fields = '__all__'