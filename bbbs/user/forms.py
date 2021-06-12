from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.mail import send_mail


CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if (
            user.is_admin_role
            or user.is_moderator_role
            or user.is_regional_moderator_role
        ):
            user.is_staff = True
        password = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        send_mail(
            subject='Получения токена',
            message=f'Пароль {password} для получения токена',
            from_email='super@super.fake',
            recipient_list=[email]
        )
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
