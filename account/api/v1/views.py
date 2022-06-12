from rest_framework.response import Response
from .serializer import UserSerializer, DeveloperSerializer, RecruterSerializer
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView
from account.models import User
from job.models import Job
from tag.models import Tag
from job.api.v1.serializer import  JobSerializer
@api_view(['POST'])
@permission_classes('')
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_signout(request):
    request.user.auth_token.delete()

    return Response({"success": "Successfully logged out."},
                    status=status.HTTP_200_OK)

@api_view(['PATCH'])
def user_update(request,user_id):
    response={'data':None,'status':status.HTTP_400_BAD_REQUEST}
    user_instance=User.objects.get(id=user_id)
    if user_instance.user_type == 'developer':
        serializer=DeveloperSerializer(instance=user_instance,data=request.data)
    elif user_instance.user_type=='recruiter':
        serializer=RecruterSerializer(instance=user_instance,data=request.data)
    else:
        serializer=None
    if serializer.is_valid():
        serializer.save()
        response['data']=serializer.data
        response['status']=status.HTTP_201_CREATED
    else:
        response["data"]=serializer.errors
    return Response(**response)

@api_view(['GET'])
def user_read(request,user_id):
    response={'data':None,'status':status.HTTP_400_BAD_REQUEST}
    user_instance=User.objects.get(id=user_id)
    if user_instance.user_type == 'developer':
        serializer=DeveloperSerializer(instance=user_instance,data=request.data)
    elif user_instance.user_type=='recruiter':
        serializer=RecruterSerializer(instance=user_instance,data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data']=serializer.data
        response['status']=status.HTTP_201_CREATED
    else:
        response["data"]=serializer.errors
    return Response(**response)


@api_view(['GET'])
def job_read(request, user_id):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    user_instance=User.objects.get(id=user_id)
    job = Job.objects.get(developer=user_instance, status='open')
    if user_instance.user_type == 'developer':
        serializer=DeveloperSerializer(instance=job,data=request.data)
    elif user_instance.user_type=='recruiter':
        serializer=RecruterSerializer(instance=job,data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data']=serializer.data
        response['status']=status.HTTP_201_CREATED
    else:
        response["data"]=serializer.errors
    return Response(**response)
