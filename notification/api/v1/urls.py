from django.urls import path
from .views import hello,get_notification

urlpatterns = [
    path('/hello',hello, name='hello'),
    path('/<int:id>',get_notification, name='get_notification'),
]