from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job.models import Job
from .serializer import NotificationSerializer
@api_view(['GET'])
def hello (request):
    return Response(data={'hi':'hi'},status=status.HTTP_200_OK)

def get_notification(request,id):
    job = Job.objects.get(pk=id)
    ser = NotificationSerializer(instance=job)
    return Response(data=ser.data, status=status.HTTP_200_OK)

# def create_notification(data):
#        serializer = JobSerializer(data=request.data)

#         if (serializer.is_valid()):
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)