from django.db import models
import datetime
# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateTimeField()
    
    def __str__(self):
        return self.name