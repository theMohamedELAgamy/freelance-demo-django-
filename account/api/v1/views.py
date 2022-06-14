from rest_framework.response import Response
from .serializer import UserSerializer, DeveloperSerializer, RecruterSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from account.models import User
from job.models import Job
from tag.models import Tag
from job.api.v1.serializer import JobSerializer
from rest_framework import generics
from django.http import JsonResponse


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
def user_update(request, user_id):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    user_instance = User.objects.get(id=user_id)
    if user_instance.user_type == 'developer':
        serializer = DeveloperSerializer(instance=user_instance, data=request.data)
    elif user_instance.user_type == 'recruiter':
        serializer = RecruterSerializer(instance=user_instance, data=request.data)
    else:
        serializer = None
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response["data"] = serializer.errors
    return Response(**response)


@api_view(['GET'])
def user_read(request, user_id):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    user_instance = User.objects.get(id=user_id)
    print(user_instance)
    if user_instance.user_type == 'developer':
         serializer = DeveloperSerializer(instance=user_instance)
    elif user_instance.user_type == 'recruiter':
        serializer = RecruterSerializer(instance=user_instance)

    return Response(serializer.data)


@api_view(['GET'])
def view_recruiter_jobs(request, user_id):
    response = {'data': None, 'status': status.HTTP_200_OK}
    user_instance = User.objects.get(id=user_id)
    if user_instance.user_type == 'recruiter':
        job = Job.objects.filter(created_by_id=user_id)
        print(job)
        serializer = JobSerializer(instance=job, many=True)
        return Response(serializer.data)
    return Response(**response)


class GetDeveloperJob(generics.ListAPIView):
    queryset = Job.objects.all()
    def list(self, request, user_id):
        try:
            job = Job.objects.get(developer_id=user_id, status="in_progress")
            serializer = JobSerializer(job)
            tags_data = serializer.data["tags"]
            print(tags_data)
            for i in tags_data:
                developer_tags = Tag.objects.get(id=i)
            return Response(serializer.data)
        except :
            return JsonResponse({'error': "No jobs"})
            pass



