from rest_framework import serializers


class HelloSerializer(serializers.Serializers):
    '''Serializers a name field for testing our APIView
    Creates a django framework serializer'''
    
    name = serializers.CharField(max_lenth=10)

