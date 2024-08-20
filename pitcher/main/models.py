from django.db import models, migrations
from django.http import HttpResponse

# Create your models here.
class Management(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'management'
    
