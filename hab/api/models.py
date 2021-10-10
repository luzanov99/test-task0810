from django.db import models
import datetime
# Create your models here.
class DataUser(models.Model):
    name=models.CharField(max_length=120)
    surname=models.CharField(max_length=120)
    uuid=models.CharField(max_length=120)
    plate_number=models.CharField(max_length=120, null=True)
    group=models.CharField(max_length=120, null=True)
    date=models.CharField(max_length=120)
    direction=models.CharField(max_length=120, null=True)
    status=models.IntegerField()
    type_passage=models.IntegerField()
    photo=models.CharField(max_length=120, null=True)
    ssync=models.BooleanField(null=True)
