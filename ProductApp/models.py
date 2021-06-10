from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
from rest_framework.authtoken.admin import User

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()
    # USERNAME_FIELD = 'name'
    def __str__(self):
        return self.name

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

