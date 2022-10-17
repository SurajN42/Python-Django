from rest_framework import serializers 
from .models import Author,Books 
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username','password'] 

    def create(self,validate_data):
        user = User.objects.create(username = validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user

class AuthorSerial(serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = '__all__' 

class BookSerial(serializers.ModelSerializer):
    class Meta:
        model = Books 
        fields = '__all__'