from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

# Create your models here.
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