from rest_framework import serializers
from User.models import User
from django.contrib.auth.hashers import make_password

class UsersSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = '__all__'