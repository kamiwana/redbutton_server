from django import forms
from .models import *
from .choices import *

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('file',)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('file',)

class LayerForm(forms.ModelForm):
#    type = forms.TypedChoiceField(
#        choices=LAYER_CHOICES,
#        required=True,
#        label="레이아웃 선택",
#        widget=forms.Select(attrs={'class': 'form-control'})
#    )
    class Meta:
        model = Layer
        fields = ('file',)

class LayerSubForm(forms.ModelForm):
    class Meta:
        model = LayerSub
        fields = ('file',)