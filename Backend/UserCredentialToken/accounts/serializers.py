from rest_framework import serializers
from accounts.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(write_only=True)
    class Meta:
        model= UserRegistration
        fields= ['username','email','password','password2','contact','address','first_name','last_name']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Password doesn't matched !!")
        return (data)
    
    def create(self, validated_data):
        user= UserRegistration.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password'],
            contact= validated_data['contact'],
            address=validated_data['address']
        )
        return user

