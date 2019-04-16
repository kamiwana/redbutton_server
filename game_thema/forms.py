from django import forms
from .models import  *
from django.forms.formsets import BaseFormSet

class GameThemaForm(forms.ModelForm):

    thema_order = forms.IntegerField(label='순서',
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'})
                                )

    thema_name = forms.CharField(label='테마',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '텍스트로 입력하세요.'})
                                )


    class Meta:
        model = GameThema
        fields = ( 'thema_order','thema_name',)

class GameThemaForm_v2(forms.Form):
    """
    Form for individual user links
    """
    thema_order = forms.IntegerField(
                    label='순서',
                    widget=forms.NumberInput(attrs={
                        'class': 'form-control', 'placeholder': '숫자로 입력하세요.',
                    }),
                    required=False)
    thema_name = forms.CharField(
                    label='테마',
                    widget=forms.TextInput(attrs={
                        'class': 'form-control', 'placeholder': '텍스트로 입력하세요.',
                    }),
                    required=False)


class BaseGameThemaFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        thema_orders = []
        thema_names = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                thema_order = form.cleaned_data['thema_order']
                thema_name = form.cleaned_data['thema_name']

                # Check that no two links have the same anchor or URL
                if thema_order and thema_name:
                    if thema_order in thema_orders:
                        duplicates = True
                        thema_orders.append(thema_order)

                    if thema_name in thema_names:
                        duplicates = True
                        thema_names.append(thema_name)

                if duplicates:
                    raise forms.ValidationError(
                        'Links must have unique anchors and URLs.',
                        code='duplicate_links'
                    )

                # Check that all links have both an anchor and URL
                if thema_name and not thema_order:
                    raise forms.ValidationError(
                        '순서를 입력하세요.',
                        code='missing_thema_order'
                    )
                elif thema_order and not thema_name:
                    raise forms.ValidationError(
                        '테마명을 입력하세요.',
                        code='missing_thema_name'
                    )