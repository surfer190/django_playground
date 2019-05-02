from __future__ import absolute_import, unicode_literals
import time

from celery import shared_task

@shared_task
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
