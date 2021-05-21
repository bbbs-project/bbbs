from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.core.mail import send_mail
from bbbs.common.models import City, Profile

from ..settings import EMAIL_HOST


admin.site.unregister(User)

MESSAGE = ('Ваш пароль для авторизации: {password}. \n' + 
           'Ваше имя для авторизации: {username}. \n' +
           'Вы можете их изменить в личном кабинете.')
SUBJECT = 'Добро пожаловать на платформу "Младшие братья младшие сестры"!'


class ProfileInline(admin.TabularInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ['email', 'username', 'last_name', 'first_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )

    def save_model(self, request, obj, form, change):
        password = obj.password
        email = obj.email
        username = obj.username
        send_mail(
            subject=SUBJECT,
            message=MESSAGE.format(password=password, username=username),
            from_email=EMAIL_HOST,
            recipient_list=[email])
        obj.save()

