from django.contrib import admin

from bbbs.common.models import City


class CityAdmin(admin.ModelAdmin):
    model = City

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff and
                                             request.user.is_admin_role)

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

admin.site.register(City, CityAdmin)
