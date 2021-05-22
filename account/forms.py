from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password1"]  # для отправки пароля почтой
        email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
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
