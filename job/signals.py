from django.db.models.signals import post_save,m2m_changed
from django.contrib.auth import get_user_model
from time import sleep
from job.models import Job
from tag.models import Tag
from account.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from .api.v1.serializer import GetJobSerializer
from notification.models import Notification
from notification.api.v1.serializer import NotificationSerializer
# from notification.api.v1.views import create_notification
from .views import get_tags
import time
# @receiver(m2m_changed,sender=Job.tags.through)
# def job_post_save_action2(sender,instance,**kwargs):
#     if instance.tags.all():
#         users= User.objects.all()
#         print('here')
#         for tag  in instance.tags.all():
#             subj= 'tags alert !!'
#             msg = f'you have a job in {tag}'
#             for user in users:
#                 if(user.user_type=='developer'):
#                     create_notification(tag,user.id,instance.id)
#                     if(user.allow_mail_notification==True):
#                         receivers=[user.email]
#                         send_mail(subject=subj,message=msg,from_email='mohamedelagame82@gmail.com',recipient_list=receivers)
#                         time.sleep(6)
            


       
@receiver(m2m_changed,sender=Job.tags.through)
def job_post_save_action(**kwargs): 
    if(kwargs.get('action')=='post_add'):
        job = kwargs.get('instance')
        tags_arr =[]
        tags_dictionary ={}
        tags=job.tags.all()
        developers_arr=[]
        selected_dev =[]
        notified_dev=[]
        for tag in tags:
            tags_arr.append(tag)
            tags_dictionary[tag.name]=1
        for tagg in tags_arr:
            users=tagg.user_set.all()
            for user in users:
                if(developers_arr.count(user)==0):
                    developers_arr.append(user)

        for user in developers_arr:
            counter=0
            for tagg in user.tags.all():
                if(tags_dictionary.get(tagg.name)):
                    counter+=1

            if(counter==len(tags_arr) and user.allow_mail_notification==True and user.user_type=='developer'):
                selected_dev.append(user.email)
            if(counter==len(tags_arr) and user.user_type=='developer'):
                notified_dev.append(user)
            for user in notified_dev:
                create_notification(tags_dictionary,user,job)


        print(notified_dev)
        print(f' d emails :    {selected_dev}')
        subj= 'New Job !!'
        msg = f'New job has been posted with your qualification {job.name}. Apply quickly'
        receivers=selected_dev
        send_mail(subject=subj,message=msg,from_email='mohamedelagame82@gmail.com',recipient_list=receivers)
        

def create_notification(tag,user_id,job):
    a=Notification(
            message=f'a job with tag {tag} is created',
            developer=user_id,
            job=job
        )
    a.save()