from django.db import models

# Create your models here.
class Wish(models.Model):
    wisher=models.CharField(max_length=100)
    wishContent=models.CharField(max_length=1000)
    reward=models.CharField(max_length=1000)
    isRealized=models.BooleanField()
