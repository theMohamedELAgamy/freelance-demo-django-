from django.contrib.auth.models import AbstractUser
from django.db import models

from tag.models import Tag
# Create your models here.
class User(AbstractUser):

    roles = (
        ('developer','developer'),
        ('recruiter','recruiter')
    )
    gen = (
        ('M','male'),
        ('F','female')
    )
    user_type = models.CharField(choices=roles,max_length=10 )
    allow_mail_notification =  models.BooleanField(verbose_name='Allow mail notification',default=True)
    gender = models.CharField(choices=gen, max_length=6)
    date_of_birth = models.DateField(verbose_name='Date of Birth',null=True)
    tags = models.ManyToManyField(Tag,null=True,blank=True)
    cv = models.FileField(upload_to='users_cv/',verbose_name='CV',null=True,blank=True)
    address = models.CharField(max_length=80,null=True,blank=True)
    history = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        # print(self.tags)
        return self.username

