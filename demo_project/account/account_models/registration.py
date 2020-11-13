from django.db import models
from uuid import uuid4


class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=False, unique=True)
    address = models.JSONField(null=True)
    password = models.CharField(max_length=255, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
