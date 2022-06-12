from django.urls import path
from .views import hello,all_jobs,create_job,update_job,delete_job

urlpatterns = [
    path('/hello',hello, name='hello'),
    path('/',all_jobs, name='all_jobs'),
    path('/create',create_job, name='create_job'),
    path('/update/<int:id>',update_job, name='update_job'),
    path('/delete/<int:id>',delete_job, name='delete_job'),





    


]