import time

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from waiting.tasks import waste_time

class WaitingViewTests(TestCase):
    '''
    Tests for the waiting views
    '''
    def test_root(self):
        '''
        Ensure going to the root view shows the waiting endpoint
        '''
        response = self.client.get('/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_index(self):
        '''
        Ensure getting the index works
        '''
        waiting_index = reverse('waiting:index')
        response = self.client.get(waiting_index)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_post_index_long(self):
        '''
        Ensure posting to the index takes a short time time
        '''
        started_at = time.time()

        waiting_index = reverse('waiting:index')
        response = self.client.post(
            waiting_index,
            data={'message': 'Hello world'}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        
        elapsed = time.time() - started_at
        self.assertLess(
            elapsed,
            2
        )

    def test_waste_time_takes_long(self):
        '''
        Ensure the waste time task, when called synchronously takes long
        '''
        started_at = time.time()
        waste_time.apply()
        elapsed = time.time() - started_at
        self.assertGreater(
            elapsed,
            5
        )
