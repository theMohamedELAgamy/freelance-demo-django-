
from rest_framework import serializers
from job.models import Job
from tag.models import Tag
from tag.serializers import TagSerializer
class JobSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
          model = Job
          fields = ['name','tags','description','created_by','status']
         # depth = 1

        #   extra_kwargs={
        #     'name' : {'required':True},
        #     'tags': {'required': True},
        #     'description': {'required': True},
        #     'created_by' : {'required':True}
        # }
        #   depth = 1






       