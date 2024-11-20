from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Passwords are hashed, so it's safe to store this length.

    # Remove 'username' from REQUIRED_FIELDS
    REQUIRED_FIELDS = []  # No need to include 'username' here

    # Set the field to be used for authentication (default is 'username')
    USERNAME_FIELD = 'username'

    # Use the custom manager for user creation
    objects = CustomUserManager()

    def __str__(self):
        return self.username
