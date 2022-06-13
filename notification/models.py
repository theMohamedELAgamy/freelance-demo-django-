from django.db import models
from account.models import User
from job.models import Job
# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=120,verbose_name='Notification Message')
    creation_time = models.DateField(auto_now_add=True)
    developer=models.ForeignKey(User,verbose_name="notified developer",related_name='notified_developer',on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(Job,verbose_name="job notified",related_name='job_notified',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.message