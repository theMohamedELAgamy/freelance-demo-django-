
from rest_framework import serializers
from job.models import Job
from account.api.v1.serializer import JobUserSerializer
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
          depth=1


