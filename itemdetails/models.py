from django.db import models

# Create your models here.
class itemdetail(models.Model):
    name=models.CharField(max_length=32)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=100)

