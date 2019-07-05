from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from django_celery_results.models import TaskResult

UUID = '57585b16-eeba-4dba-961e-73794332e95d'


class TaskViewTests(TestCase):
    '''
    Ensure the task status is returned
    '''
    def setUp(self):
        my_task = TaskResult.objects.create(
            task_id=UUID,
            task_name = 'test',
            status = 'SUCCESS',
            result = 'true',
        )
    
    def test_view_task(self):
        '''
        Ensure you can view a task
        '''
        task_url = reverse(
            'tasks:view',
            kwargs={'task_id': UUID}
        )
        response = self.client.get(task_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_view_all_tasks(self):
        '''
        Ensure you can view all tasks
        '''
        task_list_url = reverse('tasks:list')
        response = self.client.get(task_list_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
