from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


# Create your views here.
# application logic behind API


class HelloApiView(APIView):
    '''Test API View'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Return a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put delete',
            'Similar to a traditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            # or message = "Hello {0} {1} {2}.format(name, email, password)"
            message = "Hello {0}".format(name)
            return Response({"message": message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''handles updating an object. pk is primary key'''
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        '''Patch request, only updates fields privuded in the request'''
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        '''delete an object'''
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API Viewset.'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''return a hello message'''
        a_viewset = [
            'Uses Actions(list, create, retrieve, update, partial_update',
            'Automatically maps ot URLS using Router',
            'Provides more functionaluity with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a new hello message'''
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''Handles getting an object by its ID'''
            return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''handles updating an object'''
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        '''handles updating part of an object'''
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        '''handles removing an object'''
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''handles creating, creating, and updating profiles'''
        serializer_class = serializers.UserProfileSerializer
        queryset = models.UserProfile.objects.all()
