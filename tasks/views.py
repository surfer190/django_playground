from rest_framework.generics import RetrieveAPIView

from django_celery_results.models import TaskResult
from tasks.serializers import TaskSerializer


class TaskView(RetrieveAPIView):
    '''
    View a task status
    '''
    queryset = TaskResult.objects.all()
    lookup_field = 'task_id'
    serializer_class = TaskSerializer
