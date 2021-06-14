from django.contrib import admin
from .models import Question, Tag


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'tag',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin)
