import time

from django.urls import reverse
from rest_framework import generics, status
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

    def create(self, request, *args, **kwargs):
        '''
        Do something that takes a long time
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # do a long task
        completed = waste_time()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def waste_time():
    '''
    Function to simulate a long running task, it really just wastes time
    '''
    print('Starting waste time...')
    time.sleep(0.5)
    print('Done Task 1...')
    time.sleep(2)
    print('Done Task 2...')
    time.sleep(1)
    print('Waiting for task 3...')
    time.sleep(4)
    print('Done task 3')
    time.sleep(1)
    print('Completing waste time...')
    return True
