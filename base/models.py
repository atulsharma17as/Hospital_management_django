from django.db import models


# Create your models here.
class patient(models.Model):
  name=models.CharField(max_length=100)
  age=models.PositiveBigIntegerField()
  gender=models.CharField(max_length=100)
  contact=models.PositiveBigIntegerField(unique=True)
  consulting=models.CharField(max_length=100)
