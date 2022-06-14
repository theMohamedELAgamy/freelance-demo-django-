
from rest_framework import serializers
from job.models import Job
from account.api.v1.serializer import JobUserSerializer
from tag.models import Tag
class JobSerializer(serializers.ModelSerializer):
      # applied_developers=JobUserSerializer(many=True)
      class Meta:
          model = Job
          fields = '__all__'
          extra_kwargs={
            'name' : {'required':True},
            'tags': {'required': True},
            'description': {'required': True},
            'created_by' : {'required':True}

        }
          # depth=1
class TagSrializer(serializers.ModelSerializer):
    class Meta:
          model = Tag
          fields = '__all__'

class GetJobSerializer(serializers.ModelSerializer):
        # tags = TagSrializer(many=True)
        class Meta:
          model = Job
          fields ="__all__"
          depth=1


