from django.test import TestCase
from django.urls import reverse
from rest_framework import status

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
