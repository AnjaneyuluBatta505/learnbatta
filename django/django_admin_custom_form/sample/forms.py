from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        print("My custom admin Form")
        super().__init__(*args, **kwargs)

    class Meta:
        fields = ('name', 'title', 'birth_date',)
