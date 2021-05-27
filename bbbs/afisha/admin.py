from django.contrib import admin

from bbbs.afisha.models import Event, EventParticipant

admin.site.register(Event)
admin.site.register(EventParticipant)