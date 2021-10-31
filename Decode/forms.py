from django import forms
from .models import DecodedData

class DecodedDataForm(forms.ModelForm):
    class Meta:
        model=DecodedData
        fields = ('Starting_Index', 'Ghap', 'Add_a_Value', 'LengthOfString', 'ImagePath', 'Data')