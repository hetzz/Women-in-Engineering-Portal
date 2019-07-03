from django import forms
from .models import Student

class ResumeForm(forms.Form):
    resume = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )