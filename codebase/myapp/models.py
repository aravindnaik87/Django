from django.db import models
from django.contrib.auth.models import User

# from . import views
# Create your models here.

class SignupUser(models.Model):
    fName = models.CharField(max_length=40)
    lName = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    pwd = models.CharField(max_length=20)

class PostData(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length=200)
    postDescription = models.CharField(max_length=200)