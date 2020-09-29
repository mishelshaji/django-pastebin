from django.forms import (
    Form,
    PasswordInput,
    CharField,
    TextInput,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator


class LoginForm(Form):
    username = CharField(
        label="Username",
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'johndoe'
            }
        ),
        required=True, # Default is True
        validators=[
            MinLengthValidator(3)
        ]
    )

    password = CharField(
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            MinLengthValidator(4, "Password too small"),
            MaxLengthValidator(25, "Password too long")
        ]
    )