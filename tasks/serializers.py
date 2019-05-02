from rest_framework.serializers import ModelSerializer

from django_celery_results.models import TaskResult

class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('task_id', 'task_name', 'status', 'date_done', 'result')
