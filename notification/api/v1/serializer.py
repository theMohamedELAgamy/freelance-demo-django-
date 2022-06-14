import imp
from rest_framework import serializers
from notification.models import Notification
from job.api.v1.serializer import GetJobSerializer
class NotificationSerializer(serializers.ModelSerializer):
     # job=GetJobSerializer(many=True)
     class Meta:
          model = Notification
          fields = '__all__'
          depth=1

class NotificationSerializerCreate(serializers.ModelSerializer):
     # job=GetJobSerializer(many=True)
     class Meta:
          model = Notification
          fields = '__all__'
          