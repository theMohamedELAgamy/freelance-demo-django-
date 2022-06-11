from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import user_signup,user_signout
urlpatterns = [
    path('login', obtain_auth_token,name='login'),
    path('logout',user_signout,name='logout'),
    path('signup',user_signup,name='signup')
]