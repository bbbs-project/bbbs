from django.contrib import admin

from .models import City, Event


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_primary')
    search_fields = ('name',)
    list_filter = ('is_primary',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'starts_at', 'city', 'address')
    search_fields = ('title',)
    list_filter = ('booked',)
    readonly_fields = ('booked',)
    
    def get_queryset(self, request):
        '''
        for regional moderator
        '''
        qs = super().get_queryset(request)
        if request.user.is_regional_moderator_role:
            return qs.filter(city__name__in=request.user.city.values_list('name'))
        return qs

admin.site.register(City, CityAdmin)
admin.site.register(Event, EventAdmin)
