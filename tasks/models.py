from django.db import models

# Create your models here.
class Task(models.Model):
    """ The task model """
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title