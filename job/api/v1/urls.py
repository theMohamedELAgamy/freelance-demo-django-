from django.urls import path
from .views import hello,all_jobs,create_job,update_job,delete_job,apply,assign_developer,get_job_details,finish_job
# from .views import hello,all_jobs,create_job,update_job,delete_job,apply,assign_developer,finish_job

urlpatterns = [
    path('/hello',hello, name='hello'),
    path('/',all_jobs, name='all_jobs'),
    path('/<int:id>',get_job_details, name='get_job_details'),
    path('/create',create_job, name='create_job'),
    path('/update/<int:id>',update_job, name='update_job'),
    path('/delete/<int:id>',delete_job, name='delete_job'),
    path('/<id>/assign/<developer_id>',assign_developer ,name='assign'),
    path('/<id>/apply',apply,name='apply'),
    path('/<id>/finish/<user_id>',finish_job,name='finish_job')

]