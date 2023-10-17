from django.db import models

# Create your models here.
class mymodel(models.Model):
    name=models.CharField(max_length=400)
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length=100)
