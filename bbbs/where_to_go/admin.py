from django.contrib import admin

from .models import Place, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'address',
        'type_of_rest',
        'chosen',
    )
    search_fields = ('title',)


admin.site.register(Place, RecommendationAdmin)
admin.site.register(Tag, TagAdmin)
