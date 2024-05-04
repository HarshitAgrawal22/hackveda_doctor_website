from django.db import models

# Create your models here.
class Appointment(models.Model):
    name= models.CharField(max_length=255)
    phone_number=models.CharField(max_length=12)
    email=models.EmailField( max_length=254)
    date= models.DateField()
    message=models.TextField()