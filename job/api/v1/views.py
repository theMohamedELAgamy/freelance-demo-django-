from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job.models import Job
from .serializer import JobSerializer
from account.models import User
import json
from .serializer import JobSerializer,GetJobSerializer,CreateJobSerializer
from django.core.mail import send_mail
from django.dispatch import receiver
from notification.models import Notification
from notification.api.v1.serializer import NotificationSerializerCreate,NotificationSerializer
@api_view(['GET'])
def hello (request):
    return Response(data={'hi':'hi'},status=status.HTTP_200_OK)

@api_view(['GET'])
def all_jobs(request):
    jobs = Job.objects.filter(status="open").values()
    ser=GetJobSerializer(instance=jobs,many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_job(request):
        creator_id =request.data.get('created_by')
        creator = User.objects.get(pk=creator_id)
        print(creator)
        if(creator.user_type=='recruiter'):
            serializer = CreateJobSerializer(data=request.data)
            print(request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"error":"user cant create unless he/she is recruiter"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def update_job(request,id):
        job = Job.objects.get(pk=id)
        if(request.method == 'PUT'):
            serializer = JobSerializer(data=request.data,instance=job)
        else:
            serializer = JobSerializer(data=request.data, instance=job,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_job_details(request,id):
    job = Job.objects.get(pk=id)
    ser = GetJobSerializer(instance=job)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_job(request,id):
    job=Job.objects.get(pk=id)
    if (job.status=='open'):
        if Job.objects.get(pk=id).delete():
            return Response(data={'detail':'job deleted successfully'},status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={'detail':'job cant be deleted '},status=status.HTTP_403_FORBIDDEN)

#           {
#             "name":"job1",
#             "tags":"tag1",
#             "description":"descrip1",
#             "status":"finished"
            
#  }


@api_view(['PATCH'])
def apply(request,id):
    applid_dev = []
    job = Job.objects.get(pk=id)
    jobs = Job.objects.filter(status='in_progress')
    user = request.user
    if(job.status =='open'):
       app_developers= job.applied_developers.all()
       for jobb in jobs:
           print(f'developer assigned to job {jobb} is {jobb.developer}')
           if jobb.developer == user:
               print(f'applying developer name is {user}')
               print('you cant apply for a job while you have a job in progress')
               return Response(data='you cant apply for a job while you have a job in progress', status=status.HTTP_400_BAD_REQUEST)
       for developer in app_developers:
           applid_dev.append(developer.id)
           if(developer.id == user.id):
                 print('you cant assign to the same job twice')
                 return Response(data='you cant assign to the same job twice', status=status.HTTP_400_BAD_REQUEST)

       applid_dev.append(user.id)
       job.applied_developers.set(applid_dev)
       if(job):
           job.save()
           return  Response(data='done', status=status.HTTP_201_CREATED)
       else:
           return Response(data='serializer.errors', status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH'])
def assign_developer(request,id,developer_id):
    rejected_devs = []
    try:
        accepted_developer= User.objects.get(pk=developer_id)
    except:
        return Response(data='there is no such user', status=status.HTTP_400_BAD_REQUEST)
    print('0')
    job = Job.objects.get(pk=id)
    for developer in job.applied_developers.all():
        print(f' applied developer id {developer.id}   ///    accepted developer id {developer_id}')
        if(not developer.id == int(developer_id)):
            rejected_devs.append(developer.email)

    print(rejected_devs)
    if(job.created_by == request.user):
        if(job.status=='open'):
            Job.objects.filter(pk=id).update(developer=accepted_developer , status='in_progress')
            send_email(accepted_developer.email, request.user.email, job,rejected_devs)
            return  Response(data='done', status=status.HTTP_201_CREATED)

        else:
            return Response(data='this job has been assigned to somebody else', status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data='the job owner only can assign job to a user', status=status.HTTP_400_BAD_REQUEST)



def send_email(accepted_email,recruiter_email,job,rejected_devs):
    subj = 'Hired !!'
    subj2 ='Bad News !!'
    msg = f'you have been accepted to this job {job}'
    msg2 = f'sorry you are rejected '
    print(f'rejected emails {rejected_devs}')
    print(f'accepted email {accepted_email}')
    print(f'recruiter email {recruiter_email}')
    receivers = [accepted_email]
    receivers2 = rejected_devs
    send_mail(subject=subj, message=msg, from_email=recruiter_email, recipient_list=receivers)
    send_mail(subject=subj2, message=msg2, from_email=recruiter_email, recipient_list=receivers2)

@api_view(['PATCH'])
def finish_job(request,id,user_id):
    job = Job.objects.get(pk=id)
    try:
        user = User.objects.get(pk=user_id)
    except:
        return Response(data='there is no such user', status=status.HTTP_400_BAD_REQUEST)
    if(job.status=='in_progress'):
        if(job.developer == user or job.created_by == user):
            Job.objects.filter(pk=id).update(status='finished')
            finish_notification(job)
            return Response(data='done', status=status.HTTP_201_CREATED)
            
        else:
            return Response(data='you are not allowed to finish this job', status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(data='you cant finish task that is not in progress', status=status.HTTP_400_BAD_REQUEST)

def finish_notification(job):
   
    a=Notification(
            message=f'a job with name {job.name} is finished',
            developer=job.developer,
            job=job
        )
    a.save()
   