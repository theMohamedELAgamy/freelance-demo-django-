from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import User
# Register your models here.
@admin.register(User)
class AccountUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","gender","tags",'user_type')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined","date_of_birth")}),
    )

#admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
    # list_display = ("user_type", "allow_mail_notification","gender","date_of_birth","cv","address","history")






















