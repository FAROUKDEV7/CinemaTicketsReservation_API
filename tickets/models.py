from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Movie Model 
class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)



# Guest Model
class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)



# Reservation Model
class Reservation(models.Model):
    guest = models.ForeignKey(Guest , related_name="reservation" , on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie , related_name="reservation" , on_delete=models.CASCADE)



User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)