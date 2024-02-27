from django.db import models

 
class Service(models.Model):
    title = models.CharField(max_length=255)
    discription=models.TextField()

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to="Brands")