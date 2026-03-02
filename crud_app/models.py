from django.db import models

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    percentage = models.FloatField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
