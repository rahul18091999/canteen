from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    user_phno = models.BigIntegerField()
    user_pass = models.CharField(max_length=50)