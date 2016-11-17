from django.db import models

# Create your models here.
class QueueEntry(models.Model):
	data = models.CharField(max_length=200)