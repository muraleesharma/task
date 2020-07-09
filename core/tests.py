from django.test import TestCase
from .models import Task
from rest_framework.test import APIRequestFactory

class TaskTest(TestCase):

    def setUp(self):
        Task.objects.create(task='sleep',description='sleep in time',status='True')
        Task.objects.create(task='wakeup',description='early',status='False')

    def task_delete(self):
        task_object = Post.objects.get(task)
    
