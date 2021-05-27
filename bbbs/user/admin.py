from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from bbbs.common.models import Profile

from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class ProfileInline(admin.TabularInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = [
        ProfileInline,
    ]
    list_display = ('email', 'username', 'first_name', 'last_name', 'role')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'role', 'is_staff', 'is_active')}),
        ('Personal info', {'classes': ('wide',), 'fields': ('email',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username', 'role',
         'password1', 'password2')}),
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_module_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)


class ProfileAdmin(admin.ModelAdmin):
    model = Profile

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_module_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
