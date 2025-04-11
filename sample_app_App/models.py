from django.db import models

# Create your models here.


class Login(models.Model):
    login_id = models.AutoField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    usertype = models.CharField(max_length=255)




class User(models.Model):
    user_id = models.AutoField(max_length=255, primary_key=True)
    login= models.ForeignKey(Login, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    
