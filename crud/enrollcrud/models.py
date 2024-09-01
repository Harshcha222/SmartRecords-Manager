from django.db import models
class user(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=30)



# Create your models here.
