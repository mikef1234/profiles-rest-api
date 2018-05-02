from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# application logic behind API


class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        '''Return a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put delete',
            'Similar to a traditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
