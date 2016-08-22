from rest_framework import status
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from api.serializers import StackSerializer
from models import getAllUsers, get_object, create_session

import uuid
import json  

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = getAllUsers()
        serializer = StackSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StackSerializer(data = request.data)
        response_data = {}
        if serializer.is_valid():
            serializer.save()
            user = get_object(request.data['username'])
            sessionid =  create_session(user.id)
            response_data['sessionid'] = str(sessionid)

            return Response(json.dumps(response_data), status.HTTP_201_CREATED, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user.
    """

    def get(self, request, username, format=None):
        user = get_object(username)
        serializer = StackSerializer(user)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        user = get_object(username)
        serializer = StackSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        user = get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class LoginAuth(APIView):

    def post(self, request, format=None):

        user_json = request.data
        username = user_json['username']
        password = user_json['password']

        response_data = {}
        try:
            user = get_object(username)
            if user.password == password:
                sessionid =  create_session(user.id)
                response_data['sessionid'] = str(sessionid)
                return Response(json.dumps(response_data), status.HTTP_201_CREATED, content_type="application/json")
            else:
                response_data['error'] = "Password Incorrect"
                return Response(json.dumps(response_data), status.HTTP_400_BAD_REQUEST, content_type="application/json")
        except:
            response_data['error'] = "Email not found"
            return Response(json.dumps(response_data), status.HTTP_400_BAD_REQUEST, content_type="application/json")

