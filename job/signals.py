from django.db.models.signals import post_save,m2m_changed
from django.contrib.auth import get_user_model
from job.models import Job
from tag.models import Tag
from account.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from .api.v1.serializer import GetJobSerializer
from notification.api.v1.serializer import NotificationSerializer
# from notification.api.v1.views import create_notification
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
                    create_notification(tag,user.id,instance.id)
                    if(user.allow_mail_notification==True):
                        receivers=[user.email]
                        send_mail(subject=subj,message=msg,from_email='mohamedelagame82@gmail.com',recipient_list=receivers)
                        time.sleep(6)
            

def create_notification(tag,user_id,job_id):
       data={
            'message':f'a job with tag {tag} is created',
            "developer":user_id,
            'job':job_id
        }
       serializer = NotificationSerializer(data=data)
       if (serializer.is_valid()):
            serializer.save()
       
