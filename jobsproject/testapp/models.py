from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    name=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Bengalorejobs(models.Model):
    name=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Delhijobs(models.Model):
    name=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class punejobs(models.Model):
    name=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.IntegerField()


