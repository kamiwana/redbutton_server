from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from crispy_forms.helper import FormHelper
from .models import *
from game_icon.models import *
#from dal import autocomplete

class CommaSeparatedSelectInteger(forms.MultipleChoiceField):
    def to_python(self, value):
        if not value:
            return '0'
        elif not isinstance(value, (list, tuple)):
            raise ValidationError(
                self.error_messages['invalid_list'], code='invalid_list'
            )
        return ','.join([str(val) for val in value])

    def validate(self, value):
        """
        Validates that the input is a string of integers separeted by comma.
        """
        if self.required and not value:
            raise ValidationError(
                self.error_messages['required'], code='required'
            )

        # Validate that each value in the value list is in self.choices.
        for val in value.split(','):
            if not self.valid_value(val):
                raise ValidationError(
                    self.error_messages['invalid_choice'],
                    code='invalid_choice',
                    params={'value': val},
                )


    def prepare_value(self, value):
        """ Convert the string of comma separated integers in list"""
        if value in validators.EMPTY_VALUES:
            return ''
        elif isinstance(value, (list, tuple)):
            return ','.join([str(val) for val in value])
        else:
            return value.split(',')


from django.forms import modelformset_factory

GameInfoDescFormset = modelformset_factory(
    GameInfoDesc,
    can_delete=True,
    fields=('language', 'game_name',  'genre', 'genre_detail', 'cnt', 'tag', 'desc', ),
    extra=1,
    labels={
        'language': '언어',
        'game_name': '게임명',
        'genre': '장르/테마',
        'genre_detail': '세부장르',
        'cnt': '추천인원',
        'tag': '태그',
        'desc': '소개문구',
    },
    widgets={'language': forms.Select(attrs={
            'class': 'form-control',
        }),
            'game_name': forms.TextInput(attrs={
            'class': 'form-control'
        }),
            'genre': forms.TextInput(attrs={
            'class': 'form-control'
        }),
            'genre_detail': forms.TextInput(attrs={
            'class': 'form-control'
        }),
            'cnt': forms.TextInput(attrs={
            'class': 'form-control'
        }),
            'tag': forms.TextInput(attrs={
            'class': 'form-control'
        }),
            'desc': forms.Textarea(attrs={
            'class': 'form-control'
        })
    }
)

class GameInfoDescForm(forms.ModelForm):

    language = forms.ModelChoiceField(
                queryset=Language.objects.all(),
                required=True,
                label="언어",
                widget=forms.Select(attrs={'class': 'form-control'})
    )

    game_name = forms.CharField(label='게임명',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    genre = forms.CharField(label='장르/테마',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    genre_detail = forms.CharField(label='세부장르',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnt = forms.CharField(
        required=True,
        label="추천인원",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3~6명 문자열', 'max_length': '20'}),
    )

    tag = forms.CharField(label='태그',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    desc = forms.CharField(label='소개문구',
                                widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = GameInfoDesc
        fields = ['language', 'game_name',  'genre', 'genre_detail', 'cnt', 'tag', 'desc']


class GameInfo_V2Form(forms.ModelForm):
    game_id = forms.IntegerField(label='게임아이디',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}))

    game_relation = forms.CharField(label='연관추천게임(여러개 입력시 게임아이디 콤마로 구분 입력)',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    level = forms.ChoiceField(
        choices=LEVEL_TYPES,
        required=True,
        label="난이도",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    eng_title = forms.CharField(label='영어제목',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    created_date = forms.CharField(label='출시년도', widget=forms.TextInput(attrs={'class': 'form-control'}))

    min_cnt = forms.IntegerField(label='최소인원',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}))
    max_cnt = forms.IntegerField(label='최대인원',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}))
    play_time = forms.IntegerField(label='플레이시간',
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '분으로 입력하세요.'}))
    desc_time = forms.IntegerField(label='설명시간',
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '분으로 입력하세요.'}))

    game_icon = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label='아이콘',
                                               queryset=GameIcon.objects.all())
    class Meta:
        model = GameInfo
        fields = ['game_id', 'game_relation', 'level', 'eng_title', 'created_date', 'min_cnt', 'max_cnt',
                  'play_time', 'desc_time', 'game_icon']



class GameInfoForm(forms.ModelForm):
    game_id = forms.IntegerField(label='게임아이디',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}))

    game_name = forms.CharField(label='게임명',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    level = forms.ChoiceField(

        choices=LEVEL_TYPES,
        required=True,
        label="난이도",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    eng_title = forms.CharField(label='영어제목',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    created_date = forms.CharField(label='출시년도',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    genre = forms.CharField(label='장르/테마',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    genre_detail = forms.CharField(label='세부장르',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnt = forms.CharField(
        required=True,
        label="추천인원",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3~6명 문자열', 'max_length': '20'}),
    )
    min_cnt = forms.IntegerField(label='최소인원',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}))
    max_cnt = forms.IntegerField(label='최대인원',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}))
    play_time = forms.IntegerField(label='플레이시간',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '분으로 입력하세요.'}))
    desc_time = forms.IntegerField(label='설명시간',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '분으로 입력하세요.'}))

    desc = forms.CharField(label='소개문구',
                                widget=forms.Textarea(attrs={'class': 'form-control'}))
    tag = forms.CharField(label='태그',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    game_icon = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label='아이콘',
                                               queryset=GameIcon.objects.all())

    class Meta:
        model = GameInfo
        fields = ['game_id',  'game_name',  'genre', 'genre_detail', 'cnt', 'tag', 'desc', 'level', 'eng_title',
                  'created_date', 'min_cnt', 'max_cnt', 'play_time', 'desc_time', 'game_icon', 'icon']

class MovieDetailForm(forms.ModelForm):
    movie_id = forms.ChoiceField(
        choices=Movies.objects.none(),
        required=True,
        label="영상",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cnt_desc = forms.CharField(label='인원',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '텍스트로 입력하세요.'})
                                )

    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=True,
        label="언어",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    subtitle_id = forms.TypedChoiceField(
        choices=Subtitle.objects.none(),
        required=False,
        label="자막",
        empty_value=0,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = MovieDetail
        fields = ('movie_id', 'cnt_desc', 'language', 'subtitle_id')

    def __init__(self, gameinfo_id, *args, **kwargs):

        super(MovieDetailForm, self).__init__(*args, **kwargs)
        movie_list = Movies.objects.filter(gameinfo_id=gameinfo_id)
        movie_choices = [(o.pk, o.file.name[21:]) for o in movie_list]
        self.fields['movie_id'].choices = movie_choices

        subtitle_list = Subtitle.objects.filter(gameinfo_id=gameinfo_id)
        subtitle_choices = [(o.pk, o.file.name) for o in subtitle_list]
        self.fields['subtitle_id'].choices = subtitle_choices

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('file',)

class SubtitleForm(forms.ModelForm):
    class Meta:
        model = Subtitle
        fields = ('file',)

class GameImageForm(forms.ModelForm):
    class Meta:
        model = GameImage
        fields = ('file',)

class MoviesThumbnailForm(forms.ModelForm):
    order = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'readonly': 'readonly'},
            ),
        label='',
        required=False,
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'readonly': 'readonly'},
            ),
        label='',
        required=False,
    )
    time = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '시간을 입력해주세요.'
        }),
        label='',
        required=False
    )

    image = forms.ImageField(
        label='',
        required=False
    )

    class Meta:
        model = MoviesThumbnail
        fields = ('order', 'title', 'image', 'time', )

    def __init__(self, *args, **kwargs):
        super(MoviesThumbnailForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-12'

class GameInfoThemaForm(forms.ModelForm):
    thema = forms.ModelMultipleChoiceField(queryset=GameThema.objects.all(), required=False, label='테마',
                                           widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'})
                                           )

    class Meta:
        model = GameInfoThema
        exclude = ['gameinfo']


class GameFilterCreateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(GameFilterCreateForm, self).__init__(*args, **kwargs)
        for i in range(0, 14):
            self.fields['%s_people' % i] = forms.IntegerField(label='인원', widget=forms.TextInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}), initial=i + 2, )
            self.fields['%s_mix' % i] = forms.IntegerField(label='혼성', widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}), initial=0)
            self.fields['%s_male' % i] = forms.IntegerField(label='남성', widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}), initial=0)

            self.fields['%s_female' % i] = forms.IntegerField(label='여성', widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}), initial=0)

    def save(self, gameinfo_id):
        data = self.cleaned_data
        for i in range(0, 14):
            game_filter = GameFilter(gameinfo_id=gameinfo_id, people=data['%s_people' % i],
                                     mix=data['%s_mix' % i],
                                     male=data['%s_male' % i],
                                     female=data['%s_female' % i], )
            game_filter.save()


class GameFilterUpdateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        gameinfo_id = kwargs.pop('gameinfo_id', None)
        super(GameFilterUpdateForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(GameFilter.objects.filter(gameinfo=gameinfo_id)):
            self.fields['%s_people' % i] = forms.IntegerField(label='인원', widget=forms.TextInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}), initial=q.people, )
            self.fields['%s_mix' % i] = forms.IntegerField(label='혼성', widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}), initial=q.mix)
            self.fields['%s_male' % i] = forms.IntegerField(label='남성', widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}), initial=q.male)
            self.fields['%s_female' % i] = forms.IntegerField(label='여성', widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '숫자로 입력하세요.'}), initial=q.female)

    def save(self, gameinfo_id):
        data = self.cleaned_data
        for i in range(0, 14):
            game_filter = GameFilter(gameinfo_id=gameinfo_id, people=data['%s_people' % i],
                                     mix=data['%s_mix' % i],
                                     male=data['%s_male' % i],
                                     female=data['%s_female' % i], )
            game_filter.save()