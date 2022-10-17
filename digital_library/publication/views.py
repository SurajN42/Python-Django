from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Books 
from .serializers import BookSerial
from .serializers import UserSerializer
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)   
        if not serializer.is_valid():
            return Response({'errors': serializer.errors , 'message': 'Something went wrong' })
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'payload': serializer.data , 'token': str(token_obj), 'message': 'Data is saved' })


class BooksAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get(self,request):
        try:
            obj = Books.objects.all()
            serializer = BookSerial(obj, many=True) 
            return Response({'payload':serializer.data}) 
        except Exception as e:
            return Response({'payload': {} , 'message': 'There is no data'}) 

    def post(self,request):
        try:
            serializer = BookSerial(data = request.data)   
            if serializer.is_valid():
                serializer.save()
            return Response({'payload': request.data , 'message': 'Data added to database' })
        except Exception as e:
            return Response({'payload': {} , 'message': 'There is no data' })

    def put(self,request):
        try:
            obj = Books.objects.get(pk = request.data['id']) 
            serializer = BookSerial(obj , data = request.data , partial = True )
            if serializer.is_valid():
                serializer.save()
            return Response({'payload': request.data ,'message': 'Data update Successfully'})
        except Exception as e:
            return Response({'payload': {} , 'message': 'There is no data' })
    
    def delete(self,request):
        try:
            obj = Books.objects.get(pk = request.data['id'])
            obj.delete()
            return Response({'payload': request.data ,'message': 'Data delete Successfully'})
        except Exception as e:
            return Response({'payload': {} , 'message': 'There is no data' })