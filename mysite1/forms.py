from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class MyAuthenticationForm(AuthenticationForm):
    email = forms.CharField(max_length=254)

    class Meta:
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def clean_username(self):
        email = self.cleaned_data.get('email')
        if email:
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Tài khoản không chính xác")
        return email
