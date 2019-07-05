import datetime
import uuid

from django.test import TestCase

from tasks.models import Task

class TaskModelTests(TestCase):
    '''
    Tests for the task model
    '''
    def test_task_model_create(self):
        task_uuid = uuid.uuid4()
        date_time = datetime.datetime.today()
        new_task = Task.objects.create(
            task_id=task_uuid,
            task_name='hello World',
            status=Task.COMPLETE,
            result='Some result',
            date_completed=date_time
        )
        self.assertEqual(
            new_task.task_id,
            task_uuid
        )
        self.assertEqual(
            new_task.task_name,
            'hello World'
        )
        self.assertEqual(
            new_task.status,
            Task.COMPLETE
        )
        self.assertEqual(
            new_task.result,
            'Some result'
        )
        self.assertEqual(
            new_task.date_completed,
            date_time
        )
