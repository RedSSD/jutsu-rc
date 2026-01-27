from django.db import models

# Create your models here.
class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=255)