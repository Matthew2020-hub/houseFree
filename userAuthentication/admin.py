from django.contrib import admin
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin

# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'user_id', 'last_name', 'home_address', 'is_admin', 'is_staff')
#     search_fields = ('email', 'country')
#     readonly_fields = ['date_created']

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    filter_horizontal = ()
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)