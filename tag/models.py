from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(verbose_name='Tag Name',max_length=20)


    def __str__(self):
        return self.name
