from django import forms
from .models import *
class UrlForm(forms.ModelForm):
    class Meta:
        model=storage
        fields=['url']