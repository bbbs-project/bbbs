from django.contrib import admin

from bbbs.afisha.models import Event
from bbbs.common.models import City


class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'starts_at', 'city', 'address')
    search_fields = ('title',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'city' and request.user.is_regional_moderator_role:
            kwargs['queryset'] = City.objects.filter(user=request.user.profile)
        return super(EventAdmin, self).formfield_for_foreignkey(db_field,
                                                                request,
                                                                **kwargs)

    def get_queryset(self, request):
        '''
        for regional moderator
        '''
        qs = super().get_queryset(request)
        if request.user.is_regional_moderator_role:
            return qs.filter(city=request.user.profile.city_id)
        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin_role)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff


admin.site.register(Event, EventAdmin)
