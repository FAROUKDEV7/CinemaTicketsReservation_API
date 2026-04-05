from django.db import models


# Movie Model 
class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField()



# Guest Model
class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)



# Reservation Model
class Reservation(models.Model):
    guest = models.ForeignKey(Guest , related_name="reservation" , on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie , related_name="reservation" , on_delete=models.CASCADE)