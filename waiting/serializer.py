from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''
    A simple serializer
    '''
    message = serializers.CharField()
