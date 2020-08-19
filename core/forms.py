from django import forms
from .models import *


class CommentsForms(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 3,
            'cols': 24,
        }))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('user_name', 'user_email', 'message',)
