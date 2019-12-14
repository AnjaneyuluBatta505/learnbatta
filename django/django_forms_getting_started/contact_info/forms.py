from django import forms
from .models import ContacIfo

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContacIfo
        fields = ('first_name', 'last_name', 'message')
