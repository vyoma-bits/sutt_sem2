# In your models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(User):
    bits_id = models.CharField(max_length=20,unique=True)

class train(models.Model):
    name=models.ImageField(upload_to='pics')
class locations(models.Model):
    location=models.CharField(max_length=250,primary_key=True)

class trip3(models.Model):
    id=models.IntegerField(primary_key=True)
    place=models.ForeignKey(locations,on_delete=models.CASCADE)
  
    people=models.IntegerField()
    leader=models.ForeignKey(User,on_delete=models.CASCADE)
    start_date1=models.DateField()
    end_date1=models.DateField()
    expense1=models.IntegerField()

class Trip_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    trip=models.ForeignKey(trip3,on_delete=models.CASCADE)

class person(models.Model):
    bits_id=models.CharField()
    name=models.CharField(max_length=80)
    age=models.IntegerField()
    user_email=models.EmailField(max_length=250)
    user_mobile=models.CharField(max_length=30)

    expense1=models.IntegerField()
class plans(models.Model):
    trip_id=models.ForeignKey(trip3,on_delete=models.CASCADE)
    id_plan=models.IntegerField(primary_key=True)
    owner=models.ForeignKey(Trip_info,on_delete=models.CASCADE)
    description=models.CharField(max_length=250)
class events(models.Model):
    owner=models.ForeignKey(Trip_info,on_delete=models.CASCADE)
   

    id1=models.ForeignKey(plans,on_delete=models.CASCADE)
    
  
    place=models.CharField(max_length=200)
    s_time=models.TimeField(max_length=200)
    e_time=models.TimeField(max_length=200)
    estimated=models.IntegerField()
    date=models.DateField()
    description=models.CharField(max_length=200)
class expense(models.Model):
    user=models.OneToOneField(Trip_info,on_delete=models.CASCADE,primary_key=True)
    trip_id1=models.ForeignKey(trip3,on_delete=models.CASCADE)
    expense=models.IntegerField()
    expense_id=models.IntegerField()
    description=models.CharField(max_length=250)










    





   