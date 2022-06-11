from django.db import models
from tag.models import Tag
from account.models import User
# Create your models here.
class Job(models.Model):
    s = (
        ('open','open'),
        ('in_progress','in_progress'),
        ('finished','finished')
    )
    name = models.CharField(verbose_name='Job title',max_length=40)
    creation_time = models.DateField(auto_now_add=True)
    modification_time = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    description=models.fields.TextField(verbose_name='job description',default='NO Description')
    applied_developers = models.ManyToManyField('account.user',verbose_name='Applied developers',related_name='applied_developers',null=True)
    developer = models.ForeignKey(User,verbose_name='Accepted developer',on_delete=models.CASCADE,related_name='accepted_developer',null=True)
    created_by = models.ForeignKey(User,verbose_name='Job owner',on_delete=models.CASCADE ,related_name='company_name',null=True)
    status = models.CharField(choices=s,max_length=12,default='open')


