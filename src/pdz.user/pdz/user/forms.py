from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from pdz.user.models import User


class EmailUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        self.base_fields.pop('username', None)
        super(EmailUserCreationForm, self).__init__(*args, **kwargs)



class EmailUserChangeForm(UserChangeForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        self.base_fields.pop('username', None)
        super(EmailUserChangeForm, self).__init__(*args, **kwargs)
