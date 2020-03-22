from django.db import models

# Create your models here.

def upload_path(instance,filename):
    return '/'.join(['images',str(instance.name),filename])
class itemdetail(models.Model):
    name=models.CharField(max_length=32)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to=upload_path)
    desc=models.CharField(max_length=100)

