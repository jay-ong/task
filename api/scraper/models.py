import uuid
from django.db import models


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    endpoint = models.CharField(max_length=200)
    success = models.BooleanField(default=False)
    status = models.CharField(max_length=20)
    errors = models.JSONField()
    task_name = models.CharField(max_length=100)
    result = models.JSONField()
