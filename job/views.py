from django.shortcuts import render
from job.models import Job
from tag.models import Tag
from account.models import User
# Create your views here.
def get_tags(request):
    users= User.objects.all()
    for user in users :
        print(user.tags.all())


