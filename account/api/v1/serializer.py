from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

# Create your models here.
#make Developer for serializer contains developer fields only
#another serializer for company contains field only

#serializer for sign up for user
class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','password_confirm','email','user_type','gender','date_of_birth','profile_picture',]
        extra_kwargs= {
            'password':{'write_only':True},
            'email' : {'required':True},
            'date_of_birth': {'required':True},
            'profile_picture': {'required': True}

        }
    depth=1
    def save(self,**kwargs):
        print(self.validated_data['username'])
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            date_of_birth=self.validated_data['date_of_birth'],
            user_type = self.validated_data['user_type'],
            gender = self.validated_data['gender'],
            profile_picture = self.validated_data['profile_picture']
        )


        if(self.validated_data['password'] != self.validated_data['password_confirm']):
          raise  serializers.ValidationError({'details':'passwords didnt match'})


        user.set_password(self.validated_data['password'])
        user.save()
        return user


class JobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','user_type','id']
        
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username','date_of_birth','date_joined','cv','allow_mail_notification','tags']
        optional_fields=['gender',"date_of_birth","cv","tags","allow_mail_notification",'username',]
        extra_kwargs= {
            'password':{'write_only':True},
            'email' : {'required':True},
            'date_of_birth': {'required':True}

        }
        depth = 1

class RecruterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username',"allow_mail_notification"]
        optional_fields=['gender',"date_of_birth","address","history"]
        depth = 1

