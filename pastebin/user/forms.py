from django.forms import ModelForm, CharField, TextInput, Textarea, Select, PasswordInput
from .models import Post

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        # fields = ['title', 'body']
        exclude = ['created_by']

        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'My new post'
                }
            ),
            'body': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Paste the content here'
                }
            ),
            'post_type': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }