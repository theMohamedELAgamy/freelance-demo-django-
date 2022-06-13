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

# @receiver(post_save,sender=Job)
# def job_post_save_action(sender,**kwargs):
#     if(kwargs.get('created')):
#         job = kwargs.get('instance')
#         # print(job.get('id'))
#         jobd=Job.objects.get(id=job.__getattribute__('id'))
#        # tags = [tag for tag  in job.tags.all()]
#         print(jobd.tags.through)
#         print("sender")
#         users=[]
#         for tag in tags:
#             if(User.object.filter())

# #         print(f'user : {user.email}')
#         subj= 'Welcome !!'
#         msg = f'welcome {user}'
#         receivers=[user.email]
#         send_mail(subject=subj,message=msg,from_email='test.test1233345@gmail.com',recipient_list=receivers)

#m2m_changed.connect(job_post_save_action,sender=Job.tags.through)
@receiver(m2m_changed,sender=Job.tags.through)
def job_post_save_action2(sender,instance,**kwargs):
    if instance.tags.all():
        users= User.objects.all()
        print('here')
        for tag  in instance.tags.all():
            subj= 'tags alert !!'
            msg = f'you have a job in {tag}'
            for user in users:
                 receivers=[user.email]
                 print(receivers)
                 send_mail(subject=subj,message=msg,from_email='mohamedelagame82@gmail.com',recipient_list=receivers)
                 time.sleep(6)
            

