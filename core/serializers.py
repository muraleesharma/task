from rest_framework import serializers
from .models import Task

#serializer_for_Task_model
class TaskSerializer(serializers.ModelSerializer):
      class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'status')
