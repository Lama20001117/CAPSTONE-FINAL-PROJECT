from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactSupport(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    email=models.EmailField()
    msg_at=models.DateTimeField(auto_now_add=True)
