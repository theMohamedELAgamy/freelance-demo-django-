from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job.models import Job
from notification.models import Notification
from .serializer import NotificationSerializer
@api_view(['GET'])
def hello (request):
    return Response(data={'hi':'hi'},status=status.HTTP_200_OK)
@api_view(['GET'])
def get_notifications(request,id):
    notifications = Notification.objects.filter(developer=id).values()
    # ser = NotificationSerializer(instance=notifications,many=True)
    return Response(data=notifications, status=status.HTTP_200_OK)

# def create_notification(tag,user_id,job_id):
#        data={
#             'message':f'a job with tag {tag} is created',
#             "developer":user_id,
#             'job':job_id
#         }
#        serializer = NotificationSerializer(data=data)
#        if (serializer.is_valid()):
#             serializer.save()
