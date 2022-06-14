from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import user_signup,user_signout,user_update,user_read,view_recruiter_jobs,GetDeveloperJob
app_name='account_rest_v1'
urlpatterns = [
    path('login', obtain_auth_token,name='login'),
    path('logout',user_signout,name='logout'),
    path('signup',user_signup,name='signup'),
    path('profile/<int:user_id>/update',user_update,name='update'),
    path('profile/<int:user_id>/developer_job',GetDeveloperJob.as_view(),name='developer_job'),
    path('profile/<int:user_id>/recruiter_jobs', view_recruiter_jobs, name='recruiter_job'),
    path('profile/<int:user_id>',user_read,name='profile'),
]