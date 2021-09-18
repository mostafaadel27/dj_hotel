from .models import PropertyBook
from django import forms
from django.forms import ModelForm


class PropertyBookForm(forms.ModelForm):
    class Meta:
        model = PropertyBook
        fields = ['date_from','date_to','guest','childern']
        