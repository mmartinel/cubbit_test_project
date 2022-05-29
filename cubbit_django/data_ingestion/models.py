from django.db import models

STATUS_CHOICES = [('success', 'success'), ('fail', 'fail')]
DIRECTION_CHOICES = [('upload', 'upload'), ('download', 'download')]


class Event(models.Model):
    client_user_id = models.CharField(max_length=100)
    timestamp = models.BigIntegerField()
    size = models.BigIntegerField()
    time_backend = models.BigIntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='success', max_length=7)
    direction = models.CharField(choices=DIRECTION_CHOICES, default='upload', max_length=8)
    
    class Meta:
        ordering = ['client_user_id']
