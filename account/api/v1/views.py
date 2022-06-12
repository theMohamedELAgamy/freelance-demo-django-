from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
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