from django.forms import (
    Form,
    PasswordInput,
    CharField,
    EmailInput,
)
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator


class LoginForm(Form):
    email = CharField(
        label="Email ID",
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'someone@example.com'
            }
        ),
        required=True, # Default is True
        validators=[
            EmailValidator("Invalid email")
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