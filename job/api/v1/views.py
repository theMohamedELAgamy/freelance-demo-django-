from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job.models import Job
from .serializer import JobSerializer

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