from celery.result import AsyncResult
from django_celery_results.models import TaskResult
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from tasks.serializers import TaskSerializer


class TaskView(RetrieveAPIView):
    '''
    View a task status
    '''
    queryset = TaskResult.objects.all()
    lookup_field = 'task_id'
    serializer_class = TaskSerializer
    
    def retrieve(self, request, *args, **kwargs):
        task_id = str(kwargs.get('task_id'))
        try:
            instance = TaskResult.objects.get(task_id=task_id)
            serializer = self.get_serializer(instance)
        except TaskResult.DoesNotExist:
            # instance not in db check the result backend
            result = AsyncResult(task_id)
            serializer = TaskSerializer(
                result
            )
        return Response(serializer.data)
