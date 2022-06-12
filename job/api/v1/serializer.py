
from rest_framework import serializers
from job.models import Job
class JobSerializer(serializers.ModelSerializer):
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

       