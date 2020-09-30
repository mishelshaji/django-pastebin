from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Post

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title', 'body']
        # exclude = ['password']

