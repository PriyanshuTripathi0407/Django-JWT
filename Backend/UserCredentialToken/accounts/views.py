from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.models import AbstractUser
from accounts.serializers import UserRegistrationSerializer
from rest_framework import status
from accounts.models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(APIView):

    def post(self,request):
        data= request.data
        serializedData= UserRegistrationSerializer(data=data)
        if serializedData.is_valid():
            user= serializedData.save()
            return Response({
                'message':'User Created Successfully',
                'status':True,
                'data':serializedData.data
            }, status= status.HTTP_201_CREATED )
        return Response(serializedData.errors, status= status.HTTP_400_BAD_REQUEST)
    


class UserLoginView(APIView):
    def post(self, request):
        data = request.data
        username= data.get('username')
        password= data.get('password')
        email= data.get('email')
        user= UserRegistration.objects.filter(username= username,email=email).first()

        if user and user.check_password(password):
            refresh= RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status= status.HTTP_200_OK)
            
        return Response({
            'message':'Invlaid Credentials'                   
            }, status= status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):                                                                                                                             
        user= request.user
        serializedData= UserRegistrationSerializer(user)
        return Response(serializedData.data)
    