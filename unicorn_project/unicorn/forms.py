from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UnicornUser


class UnicornUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UnicornUser
        fields = ('email',)


class UnicornUserChangeForm(UserChangeForm):
    class Meta:
        model = UnicornUser
        fields = ('email',)
