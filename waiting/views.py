from django.urls import reverse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from waiting.serializer import HelloSerializer


@api_view(['GET'])
def root_view(request):
    '''
    Show the endpoints available
    '''
    if request.method == 'GET':
        return Response({
            'waiting': reverse('waiting:index'),
        })


class IndexView(generics.ListCreateAPIView):
    
    serializer_class = HelloSerializer
    
    def list(self, request, *args, **kwargs):
        '''
        Say hello
        '''
        return Response({'message': 'hello'})
