from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .choices import *
from .models import  *
from branch.models import *

class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="ID",
        widget = forms.TextInput(attrs={'class': 'form-control', 'help_text': ''}),
        )

    password1 = forms.CharField(
        required=True,
        label="비밀번호",
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '숫자와 문자를 포함해 8자리 이상을 입력해주세요'}),
        )

    password2 = forms.CharField(
        required=True,
        label="비밀번호 확인",
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '같은 비밀번호를 다시 입력해주세요.'}),
        )

    email = forms.EmailField(
        required=True,
        label="이메일",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이메일 주소를 입력해주세요'}),
        )

    phone_number = forms.CharField(
        required=True,
        label="연락처",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    auth = forms.ChoiceField(
        choices=AUTH_CHOICES,
        required=True,
        label="권한",
        widget=forms.Select(attrs={'class': 'form-control'})

    )

    branch = forms.ChoiceField(
        choices=Branch.objects.values_list('id', 'branch_name'),
        required=True,
        label="소속지점",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    room_number = forms.IntegerField(
        required=True,
        label="방번호",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력해주세요'}),
    )

    first_name = forms.CharField(
        required=True,
        label="이름",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    username = forms.CharField(
        required=True,
        label="아이디",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username','password1', 'password2', 'email','auth', 'first_name','branch', 'room_number', 'phone_number' )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('branch', 'room_number', 'auth', 'phone_number')

    phone_number = forms.CharField(
        required=True,
        label="연락처",
        widget = forms.TextInput(attrs={'class': 'form-control'}),
        )
    
    auth = forms.ChoiceField(
        choices=AUTH_CHOICES,
        required=True,
        label="권한",
        widget=forms.Select(attrs={'class': 'form-control'})

    )

    branch = forms.ChoiceField(
        choices=Branch.objects.values_list('id', 'branch_name'),
        required=True,
        label="소속지점",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    room_number = forms.CharField(
        required=True,
        label="방번호",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력해주세요'}),
        )


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label="아이디",
        widget = forms.TextInput(attrs={'class': 'form-control', 'help_text': ''}),
        )

    first_name = forms.CharField(
        required=True,
        label="이름",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    email = forms.EmailField(
        required=True,
        label="이메일",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이메일 주소를 입력해주세요'}),
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')


class ResetPasswordForm(forms.ModelForm):
    password1 = forms.CharField(
        required=True,
        label="비밀번호",
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '숫자와 문자를 포함해 8자리 이상을 입력해주세요'}),
        )

    password2 = forms.CharField(
        required=True,
        label="비밀번호 확인",
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '같은 비밀번호를 다시 입력해주세요.'}),
        )

    class Meta:
        model = User
        fields = ('password1', 'password2')