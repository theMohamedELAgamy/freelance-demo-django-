from django.db.models.signals import post_save,m2m_changed
from django.contrib.auth import get_user_model
from job.models import Job
from tag.models import Tag
from account.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from .api.v1.serializer import GetJobSerializer
from .views import get_tags
import time
@receiver(m2m_changed,sender=Job.tags.through)
def job_post_save_action2(sender,instance,**kwargs):
    if instance.tags.all():
        users= User.objects.all()
        print('here')
        for tag  in instance.tags.all():
            subj= 'tags alert !!'
            msg = f'you have a job in {tag}'
            for user in users:
                if(user.user_type=='developer'):
                    receivers=[user.email]
                    print(receivers)
                    send_mail(subject=subj,message=msg,from_email='mohamedelagame82@gmail.com',recipient_list=receivers)
                    time.sleep(6)
            

