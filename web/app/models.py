from django.db import models

class Contact(models.Model):
    first_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    email=models.EmailField()
    contect=models.TextField(max_length=300)
# Create your models here.
