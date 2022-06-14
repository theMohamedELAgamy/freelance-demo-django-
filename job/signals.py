from time import sleep

from django.db.models.signals import m2m_changed
from job.models import Job
from django.core.mail import send_mail
from django.dispatch import receiver
@receiver(m2m_changed,sender=Job.tags.through)
def job_post_save_action(**kwargs):
    # print('before if')
    # print(f'kwargs{kwargs} ')
    if(kwargs.get('action')=='post_add'):
        job = kwargs.get('instance')
        tags_arr =[]
        tags_dictionary ={}
        tags=job.tags.all()
        developers_arr=[]
        selected_dev =[]
        for tag in tags:
            tags_arr.append(tag)
            tags_dictionary[tag.name]=1
        for tagg in tags_arr:
            users=tagg.user_set.all()
            for user in users:
                print(f'user {user} count is {developers_arr.count(user)}')
                if(developers_arr.count(user)==0):
                    developers_arr.append(user)

        print(f'users who have any same tag {developers_arr}')
        print(f' dictionary :{tags_dictionary}')
        for user in developers_arr:
            counter=0
            for tagg in user.tags.all():
                if(tags_dictionary.get(tagg.name)):
                    counter+=1

            if(counter==len(tags_arr)):
                selected_dev.append(user.email)


        print(f' selected emails :    {selected_dev}')
        subj= 'New Job !!'
        msg = f'New job has been posted with your qualification {job}. Apply quickly'
        receivers=selected_dev
        # send_mail(subject=subj,message=msg,from_email='test.test1233345@gmail.com',recipient_list=receivers)