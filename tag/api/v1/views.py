from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from tag.models import Tag
from .serializers import TagSerializer


@api_view(['GET'])
@permission_classes('')
def get_tags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(instance=tags,many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

