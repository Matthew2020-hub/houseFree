from django.contrib import admin
from .models import User

from django.contrib.auth.admin import UserAdmin

# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'user_id', 'last_name', 'home_address', 'is_admin', 'is_staff')
#     search_fields = ('email', 'country')
#     readonly_fields = ['date_created']

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
# Register your models here.

admin.site.register(User)