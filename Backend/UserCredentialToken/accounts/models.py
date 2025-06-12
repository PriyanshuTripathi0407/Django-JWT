from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserRegistration(AbstractUser):
    address= models.TextField(max_length=150)
    contact= models.CharField(max_length=10)    

    def __str__(self):
        return f"({self.username} {self.password} {self.email})"

