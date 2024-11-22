from django.db import models
import uuid
class Catagerymodule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255,blank=True,default='')
    Description=models.TextField(blank=True,default='')
    Metirial=models.TextField(blank=True,default='')


# Create your models here.
