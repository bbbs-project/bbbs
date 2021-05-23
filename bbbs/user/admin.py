from django.contrib import admin
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Admin


User = get_user_model()


class AdminInline(admin.TabularInline):
    model = Admin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = [
        AdminInline,
    ]
    list_display = ('email', 'username', 'first_name', 'last_name', 'role')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role', 'is_staff', 'is_active')}),
        ('Personal info', {'classes': ('wide',), 'fields': ('email',)}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username', 'role',
         'is_staff', 'is_superuser', 'password1', 'password2')}),
        #('Advanced options', {'classes': ('wide',), 'fields': ('role', ),}),
    )
    


admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin)
