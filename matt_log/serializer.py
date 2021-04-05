# coding: utf-8

from rest_framework import serializers

from .models import User, Matt, Log_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','name','mail')

class MattSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matt
        fields = ('matt_id', 'name')

class Log_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_data
        fields = ('s_matt_id', 'created_at', 'weight', 'quantity')
