from django.contrib import admin

# Register your models here.
from .models import Job
#admin.site.register(Job)
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("name", "developer","creation_time","modification_time","developer","created_by","status",'id')
    list_filter = ("name","status")
    search_fields = ('developer__username','created_by__username')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True


    def has_change_permission(self, request, obj=None):
        return True


