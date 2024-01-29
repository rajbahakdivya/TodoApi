from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .manager import UserManager
from datetime import datetime

class User(AbstractUser):
    username= None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expires_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    # def save(self, *args, **kwargs):
    #     if not self.username:
    #         self.username = self.email
    #     super().save(*args, **kwargs)

    def name(self):
        return self.first_name + '' + self.last_name
    
    def __str__(self):
        return self.email
    
    # def save(self, *args, **kwargs):
    #     if not self.username:
    #         self.username = self.email
    #     # if not self.pk:  
    #     #     self.otp_code = get_random_string(length=6)  
    #     super().save(*args, **kwargs)