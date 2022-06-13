from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job.models import Job
from .serializer import JobSerializer
from account.models import User
import json
@api_view(['GET'])
def hello (request):
    return Response(data={'hi':'hi'},status=status.HTTP_200_OK)

@api_view(['GET'])
def all_jobs(request):
    jobs = Job.objects.filter(status="open").values()
    ser=JobSerializer(instance=jobs,many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_job(request):
        print(request.data)
        serializer = JobSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['DELETE'])
def delete_job(request,id):
    if Job.objects.get(pk=id).delete():
        return Response(data={'detail':'job deleted successfully'},status=status.HTTP_204_NO_CONTENT)
#              {
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
    try:
        user = User.objects.get(pk=developer_id)
    except:
        return Response(data='there is no such user', status=status.HTTP_400_BAD_REQUEST)
    job = Job.objects.get(pk=id)
    if(job.status=='open'):
            Job.objects.filter(pk=id).update(developer=user , status='in_progress')

            return  Response(data='done', status=status.HTTP_201_CREATED)

    else:
        return Response(data='this job has been assigned to somebody else', status=status.HTTP_400_BAD_REQUEST)




