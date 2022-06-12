from django.db.models.signals import post_save
from job.models import Job
from django.core.mail import send_mail
from django.dispatch import receiver
@receiver(post_save,sender=Job)
def job_post_save_action(**kwargs):
    if(kwargs.get('created')):
        job = kwargs.get('instance')
        tags=job.tags.all()
#         users=[]
#         for tag in tags:
#             if(User.object.filter())

# #         print(f'user : {user.email}')
#         subj= 'Welcome !!'
#         msg = f'welcome {user}'
#         receivers=[user.email]
#         send_mail(subject=subj,message=msg,from_email='test.test1233345@gmail.com',recipient_list=receivers)