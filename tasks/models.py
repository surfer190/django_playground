from django.db import models


class Task(models.Model):
    '''
    Model for a task
    '''
    COMPLETE = 'COMPLETE'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    OTHER = 'OTHER'
    STATUS_CHOICES = (
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed'),
        (PENDING, 'Pending'),
        (OTHER, 'Other'),
    )
    
    task_id = models.UUIDField()
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    task_name = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    date_completed = models.DateTimeField(
        null=True,
        blank=True
    )



