from django import forms
from .models import  *
from branch.models import *

class BranchForm(forms.ModelForm):
    branch_code = forms.CharField(
        required=True,
        label="아이디",
        widget = forms.TextInput(attrs={'class': 'form-control'}),
        )
    branch_name = forms.CharField(
        required=True,
        label="이름",
        widget = forms.TextInput(attrs={'class': 'form-control'}),
        )
    phone_number = forms.CharField(
        required=False,
        label="연락처",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    branch_user = forms.CharField(
        required=False,
        label="담당자",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    branch_address = forms.CharField(
        required=False,
        label="주소",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    is_together = forms.BooleanField(
        required=False,
        label="투게더",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    is_together = forms.BooleanField(
        required=False,
        label="투게더",
        widget=forms.CheckboxInput(),
    )
    is_note = forms.BooleanField(
        required=False,
        label="쪽지허용",
        widget=forms.CheckboxInput(),
    )
    is_forbidden_word = forms.BooleanField(
        required=False,
        label="금지어알람",
        widget=forms.CheckboxInput(),
    )
    is_desc_request = forms.BooleanField(
        required=False,
        label="직원설명 요청",
        widget=forms.CheckboxInput(),
    )
    forbidden_word_cnt = forms.IntegerField(
        required=False,
        label="연속횟수",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력해주세요.'}),
    )
    forbidden_word_scope = forms.IntegerField(
        required=False,
        label="영상볼륨",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력해주세요.'}),
    )
    system_volume = forms.IntegerField(
        required=False,
        label="시스템볼륨",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력해주세요.'}),
    )
    class Meta:
        model = Branch
        fields = ('branch_code', 'branch_name', 'phone_number', 'branch_user', 'branch_address', 'is_together', 'is_note', 'is_forbidden_word','is_desc_request','forbidden_word_cnt','forbidden_word_scope','system_volume')

