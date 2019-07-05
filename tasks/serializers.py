from rest_framework.serializers import ModelSerializer

from django_celery_results.models import TaskResult
from tasks.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('task_id', 'task_name', 'status', 'date_done', 'result')


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_id', 'status', 'task_name' , 'result', 'date_completed')
