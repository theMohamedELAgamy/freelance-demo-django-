from django.contrib import admin

# Register your models here.
from .models import User
#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_type", "allow_mail_notification","gender","date_of_birth","cv","address","history")

