from django.db import models


#task_model
class Task(models.Model):
      task = models.CharField(max_length=120)
      description = models.TextField()
      status = models.BooleanField(default=False)

      def _str_(self):
        return self.task
