from django import forms
from .models import *

class etcForm(forms.ModelForm):
    mail_address = forms.CharField(
        required=False,
        label="고객의견 알림 e-mail 등록",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'test01@gmail.com;test02@gmail.com; 형식으로 입력하세요.'}),
        )

    movie_watch_cnt = forms.IntegerField(
        required=False,
        label="영상 연속시청가능 횟수",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1~100 숫자로 입력하세요.'}),
        )

    volume_settting = forms.IntegerField(
        required=False,
        label="i-Pad 볼륨 설정",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1~100 숫자로 입력하세요.'}),
        )

    class Meta:
        model = Etc
        fields = ('mail_address','movie_watch_cnt','volume_settting',)
