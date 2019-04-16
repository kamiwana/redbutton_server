from django import forms
from .models import  *

class BranchGameForm(forms.ModelForm):

    class Meta:
        model = BranchGame
        fields = ('__all__')

