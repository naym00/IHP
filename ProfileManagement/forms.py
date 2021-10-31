from django import forms
from .models import ProfileInformation

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileInformation
        fields = ('nickname', 'profilepic', 'coverpic')