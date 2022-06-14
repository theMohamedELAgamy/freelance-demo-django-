from django.urls import path
from .views import hello,get_notifications

urlpatterns = [
    path('/hello',hello, name='hello'),
    path('/<int:id>',get_notifications, name='get_notifications'),
]