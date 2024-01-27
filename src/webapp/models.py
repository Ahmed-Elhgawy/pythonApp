from django.db import models

# Create your models here.
class UserIP(models.Model):
    public_ip = models.GenericIPAddressField(unique=True)
