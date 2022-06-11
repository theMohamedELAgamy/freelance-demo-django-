from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=120,verbose_name='Notification Message')
    creation_time = models.DateField(auto_now_add=True)