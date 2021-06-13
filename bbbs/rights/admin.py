from django.contrib import admin

from .models import Right


class RightAdmin(admin.ModelAdmin):
    model = Right

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin_role)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin_role)

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff


admin.site.register(Right, RightAdmin)
