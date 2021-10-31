from django import forms
from .models import EncodedData

class EncodedDataForm(forms.ModelForm):
    class Meta:
        model=EncodedData
        fields = ('Starting_Index', 'Ghap', 'Add_a_Value', 'HiddenData', 'SavingPath', 'LengthOfString')