from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import City, Event


User = get_user_model()


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_primary')
    search_fields = ('name',)
    list_filter = ('is_primary',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'starts_at', 'city', 'address')
    search_fields = ('title',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'city' and request.user.is_regional_moderator_role:
            kwargs['queryset'] = City.objects.filter(user=request.user)
        return super(EventAdmin, self).formfield_for_foreignkey(db_field,
                                                                request,
                                                                **kwargs)

    def get_queryset(self, request):
        '''
        for regional moderator
        '''
        qs = super().get_queryset(request)
        if request.user.is_regional_moderator_role:
            return qs.filter(city__in=request.user.city.all())
        return qs


admin.site.register(City, CityAdmin)
admin.site.register(Event, EventAdmin)
