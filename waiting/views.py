from django.urls import reverse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from waiting.serializer import HelloSerializer
from waiting import tasks


@api_view(['GET'])
def root_view(request):
    '''
    Show the endpoints available
    '''
    if request.method == 'GET':
        return Response({
            'waiting': reverse('waiting:index', request=request),
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
        waste_time_task = tasks.waste_time.delay()
        task_id = waste_time_task.task_id
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'task_id': task_id,
                'href': reverse('tasks:view', args=[task_id], request=request)
            },
            status=status.HTTP_202_ACCEPTED,
            headers=headers
        )
