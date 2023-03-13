from django.contrib import admin
from user.models import myuser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class UserInline(admin.StackedInline):
#     model=user
#     can_delete=False
#     verbose_name_plural='Users'
# class CustomizedUserAdmin(UserAdmin):
#     inlines=(UserInline,)

#admin.site.unregister(User)
# admin.site.register(User,CustomizedUserAdmin)
admin.site.register(myuser)
