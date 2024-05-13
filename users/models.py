from django.contrib.auth.models import User
from django.db import models

class Users(models.Model):
    info = models.OneToOneField(User,null=False,on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50,default="",blank=True)
    reset_password_expire = models.DateTimeField(null=True,blank=True)
    active = models.BooleanField(default=True,null=False)
    
