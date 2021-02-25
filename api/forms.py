from django import forms
from . models import student

class studentForm(forms.ModelForm):
    class Meta:
        fields=('name','roll','city')