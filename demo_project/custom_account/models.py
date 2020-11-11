from django.db import models
from typing import Dict
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: None):
        if email is None:
            raise TypeError(f'email should not be None')

        user = self.model(email=self.normalize_email(email=email))
        user.set_password(password)
        user.save()
        return user


class UserCredentials(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    email = models.EmailField(max_length=120, unique=True, null=False, db_index=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


