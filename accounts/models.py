from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # We won't be using username, email, or passsword fields here since we are inheriting Abstract User
    # Django already has a User model with those fields in it, so we just need to extend it
    fullname = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname